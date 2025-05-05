#!/usr/bin/env python3

from llama_index.core import Settings, SimpleDirectoryReader, StorageContext
from llama_index.core import VectorStoreIndex
from llama_index.core.callbacks import CallbackManager, TokenCountingHandler
from llama_index.core.ingestion import IngestionPipeline
from llama_index.core.node_parser import SentenceSplitter
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.retrievers.bm25 import BM25Retriever

from collections import Counter
from datetime import datetime
import json
import logging
import os
import pandas as pd
from pathlib import Path
import sys
import re
import tiktoken

from readers import CustomReader
from utils import get_vector_store

logger = logging.getLogger(__name__)
logging.getLogger("httpx").setLevel(logging.WARNING)


def get_tokenizer_and_model(llm_name, embed_model_name):
    logger.info("Model parameters:")
    logger.info(f"{llm_name=}")
    logger.info(f"{embed_model_name=}")

    # Tokenizer

    tokenizer = tiktoken.encoding_for_model(model_name=llm_name).encode
    Settings.tokenizer = tokenizer

    token_counter = TokenCountingHandler()
    Settings.callback_manager = CallbackManager([token_counter])
     
    # Embedding model

    embed_model = OpenAIEmbedding(model=embed_model_name)
    Settings.embed_model = embed_model

    return tokenizer, token_counter, embed_model


def get_input_files(input_dir):
    input_files = [file for file in Path(input_dir).rglob("*.md")
            if os.path.isfile(file)]

    counter = Counter(file.parts[2] for file in input_files)
    logger.info(f"Found {sum(counter.values())} files:")

    items = sorted(counter.items(), key=lambda item: item[1], reverse=True)
    for key, value in items:
        logger.info(f"{key}: {value}")

    return input_files


def get_documents(
        input_dir, tokenizer, output_format="original",
        include_metadata=False, only_hosted=False, show_progress=False,
        ):
    logger.info("Data connector parameters:")
    logger.info(f"{output_format=}")

    input_files = get_input_files(input_dir)
    reader = CustomReader()

    start = datetime.now()
    documents = reader.load_data(
            input_files,
            output_format=output_format,
            include_metadata=include_metadata,
            only_hosted=only_hosted,
            show_progress=show_progress,
            )
    end = datetime.now()

    logger.info(f"Produced {len(documents)} documents in: {end - start}")
    document_sizes = [len(tokenizer(document.get_content()))
            for document in documents]
    logger.info("Document size statistics:\n"
            + str(pd.Series(document_sizes).describe()))

    return documents


def get_node_parser(chunk_size, chunk_overlap, tokenizer):
    logger.info("Node parser parameters:")
    logger.info(f"{chunk_size=}")
    logger.info(f"{chunk_overlap=}")

    node_parser = SentenceSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            tokenizer=tokenizer,
            )

    return node_parser


def get_nodes(documents, pipeline, tokenizer, show_progress=False):
    start = datetime.now()
    nodes = pipeline.run(documents=documents, show_progress=show_progress)
    end = datetime.now()

    logger.info(f"Produced {len(nodes)} nodes in: {end - start}")

    node_sizes = [len(tokenizer(node.get_content())) for node in nodes]
    logger.info("Node size statistics:\n"
            + str(pd.Series(node_sizes).describe()))

    return nodes


def get_vector_index(
        nodes, collection_name, client_kwargs, use_async=False,
        show_progress=False,
        ):
    vector_store = get_vector_store(
            collection_name=collection_name,
            client_kwargs=client_kwargs,
            )
    vector_store.clear()

    storage_context = StorageContext.from_defaults(
            vector_store=vector_store)

    start = datetime.now()
    vector_index = VectorStoreIndex(
            nodes=nodes,
            use_async=True,
            storage_context=storage_context,
            show_progress=True,
            )
    end = datetime.now()

    logger.info(f"Built vector index in: {end - start}")

    return vector_index


def get_bm25_retriever(nodes, persist_dir):
    start = datetime.now()
    bm25_retriever = BM25Retriever.from_defaults(nodes=nodes)
    end = datetime.now()
    logger.info(f"Built BM25 retriever in: {end - start}")

    bm25_retriever.persist(persist_dir)
    logger.info(f"BM25 retriever persisted in: {persist_dir}")


def log_token_counts(token_counter):
    logger.info(
            "Embedding tokens used: "
            f"{token_counter.total_embedding_token_count}"
            )
    logger.info(
            f"LLM tokens used: {token_counter.total_llm_token_count}"
            )


def main():
    # Basic configuration

    chunk_size = 1024
    chunk_overlap = 20

    collection_name = f"csc_{chunk_size}_{chunk_overlap}"

    # Environment variables

    with open("env.json") as file:
        os.environ.update(json.load(file))

    # Logging

    log_dir = "logs/index"
    log_file = f"{log_dir}/{collection_name}.log"

    print("Logging run in:", log_file)

    os.makedirs(log_dir, exist_ok=True)
    logging.basicConfig(
            filename=log_file, filemode="w", level=logging.INFO)
    logger.info(datetime.now())

    # Tokenizer and model

    tokenizer, token_counter, embed_model = get_tokenizer_and_model(
            llm_name="gpt-4o-mini",
            embed_model_name="text-embedding-3-small",
            )

    # Documents

    documents = get_documents(
            input_dir="data/knowledge-base",
            tokenizer=tokenizer,
            output_format="original",  # ["original", "html", "plaintext"]
            include_metadata=True,
            only_hosted=False,
            show_progress=True,
            )

    # Node parser

    node_parser = get_node_parser(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            tokenizer=tokenizer,
            )

    # Ingestion pipeline

    pipeline = IngestionPipeline(transformations=[node_parser])

    # Nodes

    nodes = get_nodes(documents, pipeline, tokenizer, show_progress=True)

    # Vector index

    client_kwargs = {
            "host": "localhost",
            "grpc_port": 6334,
            "prefer_grpc": True,
            }
    vector_index = get_vector_index(
            nodes=nodes,
            collection_name=collection_name,
            client_kwargs=client_kwargs,
            use_async=True,
            show_progress=True,
            )

    # BM25 index

    get_bm25_retriever(nodes, persist_dir=f"data/bm25/{collection_name}")

    # Token counts

    log_token_counts(token_counter)


if __name__ == "__main__":
    main()
