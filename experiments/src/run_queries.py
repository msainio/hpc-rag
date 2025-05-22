#!/ur/bin/env python3

from llama_index.core import Settings, VectorStoreIndex
from llama_index.core import get_response_synthesizer
from llama_index.core.callbacks import CallbackManager, TokenCountingHandler
from llama_index.core.postprocessor import LongContextReorder
from llama_index.core.postprocessor import SentenceTransformerRerank
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core.retrievers import QueryFusionRetriever
from llama_index.core.schema import QueryBundle

from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.llms.openai import OpenAI
from llama_index.retrievers.bm25 import BM25Retriever

import asyncio
from datetime import datetime
import json
import logging
import os
import pandas as pd
from pathlib import Path
import sys
import tiktoken
from tqdm.asyncio import tqdm_asyncio

from utils import get_vector_store

logger = logging.getLogger(__name__)
logging.getLogger("httpx").setLevel(logging.WARNING)


def get_token_counter_and_models(llm_name, embed_model_name):
    logger.info("Model parameters:")
    logger.info(f"llm_name={llm_name}")
    logger.info(f"embed_model_name={embed_model_name}")

    # Tokenizer and LLM

    tokenizer = tiktoken.encoding_for_model(model_name=llm_name).encode
    Settings.tokenizer = tokenizer

    token_counter = TokenCountingHandler()
    Settings.callback_manager = CallbackManager([token_counter])

    llm = OpenAI(model=llm_name, temperature=0.0)
    Settings.llm = llm

    # Embedding model

    embed_model = OpenAIEmbedding(model=embed_model_name)
    Settings.embed_model = embed_model

    return token_counter, llm, embed_model


def get_vector_index(collection_name, client_kwargs):
    vector_store = get_vector_store(collection_name, client_kwargs)
    vector_index = VectorStoreIndex.from_vector_store(
            vector_store=vector_store)

    return vector_index


def get_retriever(vector_index, bm25_dir, top_k=2, top_m=1):
    logger.info("Retriever parameters:")
    logger.info(f"{top_k=}")
    logger.info(f"{top_m=}")

    retrievers = []

    # top_m == 0: return top k items retrieved using BM25
    # top_m == 1: return top k items retrieved using vector search
    # top_m > 1: retrieve top k items from both indices, fuse and return top m

    if top_m == 0:
        bm25_retriever = BM25Retriever.from_persist_dir(bm25_dir)
        bm25_retriever.similarity_top_k = top_k
        retrievers.append(bm25_retriever)
        mode = "simple"
    elif top_m == 1:
        vector_retriever = vector_index.as_retriever(similarity_top_k=top_k)
        retrievers.append(vector_retriever)
        mode = "simple"
    elif top_m > 1:
        bm25_retriever = BM25Retriever.from_persist_dir(bm25_dir)
        bm25_retriever.similarity_top_k = top_m

        vector_retriever = vector_index.as_retriever(similarity_top_k=top_m)

        retrievers.append(bm25_retriever)
        retrievers.append(vector_retriever)
        mode = "reciprocal_rerank"

    retriever =  QueryFusionRetriever(
            retrievers=retrievers,
            llm=Settings.llm,
            mode=mode,
            similarity_top_k=top_k,
            num_queries=1,  # set this to 1 to disable query generation
            use_async=True,
            verbose=True,
            )

    return retriever


def get_query_engine(retriever, llm):
    response_synthesizer = get_response_synthesizer(
            llm=llm, response_mode="compact")

    query_engine = RetrieverQueryEngine(
            retriever=retriever,
            response_synthesizer=response_synthesizer,
            )

    return query_engine


def get_postprocessors(rerank_model, top_n=0):
    logger.info("Postprocessing parameters:")
    logger.info(f"top_n={top_n}")

    node_postprocessors = []

    if top_n > 0:
        reranker = SentenceTransformerRerank(model=rerank_model, top_n=top_n)
        node_postprocessors.append(reranker)

    return node_postprocessors


async def arun_queries(queries, query_engine, node_postprocessors):
    retrieval_tasks = [
            query_engine.aretrieve(QueryBundle(query_str))
            for query_str in queries
            ]

    start = datetime.now()
    nodes = await tqdm_asyncio.gather(*retrieval_tasks, desc="retrieval")
    for node_postprocessor in node_postprocessors:
        nodes = [
                node_postprocessor.postprocess_nodes(
                    nodes[i], query_bundle=QueryBundle(queries[i]))
                for i in range(len(nodes))
                ]
    end = datetime.now()

    logger.info(f"Retrieval completed in: {end - start}")

    synthesis_tasks = [
            query_engine._response_synthesizer.asynthesize(
                query=queries[i], nodes=nodes[i])
            for i in range(len(queries))
            ]

    start = datetime.now()
    responses = await tqdm_asyncio.gather(*synthesis_tasks, desc="synthesis")
    end = datetime.now()

    logger.info(f"Synthesis completed in: {end - start}")

    return responses


def log_token_counts(token_counter):
    logger.info(
            "Embedding tokens used: "
            f"{token_counter.total_embedding_token_count}"
            )
    logger.info(
            f"LLM tokens used: {token_counter.total_llm_token_count}"
            )


def main():
    # Experiment configuration

    with open("config.json") as file:
        os.environ.update(json.load(file))

    run_name = (
            f"csc_{os.environ['CHUNK_SIZE']}_{os.environ['CHUNK_OVERLAP']}_"
            f"k{k}_m{m}_n{n}_{os.environ['RERANK_MODEL'].split('/')[-1]}"
            )

    # Logger

    num_runs = sum(run_name in file for file in os.listdir("responses"))
    log_dir = "logs/query"
    log_file = f"{log_dir}/{run_name}.log"

    print("Logging run in:", log_file)

    os.makedirs(log_dir, exist_ok=True)
    logging.basicConfig(
            filename=log_file, filemode="w", level=logging.INFO)
    logger.info(datetime.now())

    # Token counter and models

    token_counter, llm, embed_model = get_token_counter_and_models(
            llm_name=os.environ["LLM_NAME"],
            embed_model_name=os.environ["EMBED_MODEL_NAME"],
            )

    # Vector index

    client_kwargs = {
            "host": "localhost",
            "grpc_port": 6334,
            "prefer_grpc": True,
            }

    vector_index = get_vector_index(
            collection_name=collection_name,
            client_kwargs=client_kwargs,
            )

    # Retriever

    retriever = get_retriever(
            vector_index=vector_index,
            bm25_dir=f"data/bm25/{collection_name}",
            top_k=k,
            top_m=m,
            )

    # Query engine

    query_engine = get_query_engine(retriever, llm)

    # Node postprocessors

    node_postprocessors = get_postprocessors(rerank_model, top_n=n)

    # Load dataset

    dataset = pd.read_json(os.environ["DATASET"])

    # Retrieve

    queries = dataset["question"].to_list()

    responses = asyncio.run(
            arun_queries(queries, query_engine, node_postprocessors)
            )

    dataset["response"] = [response.response for response in responses]
    dataset["source_nodes"] = [
            [
                {
                    "file_path": node.metadata["file_path"],
                    "content": node.text,
                    "score": node.score,
                    }
                for node in response.source_nodes
                ]
            for response in responses
            ]

    # Token counts

    log_token_counts(token_counter)

    # Save results

    output_dir = Path("generations")
    file_name = f"{run_name}.json"
    output_file = output_dir / file_name

    os.makedirs(output_dir, exist_ok=True)

    dataset.to_json(
            output_file,
            orient="records",
            force_ascii=False,
            indent=4,
            )

    logger.info(f"Generations saved to: {output_file}")


if __name__ == "__main__":
    main()
