#!/usr/bin/env python3

from llama_index.llms.openai import OpenAI
from llama_index.core.prompts import PromptTemplate

import asyncio
import json
import os
import openai
import pandas as pd
from pathlib import Path
from tqdm.asyncio import tqdm_asyncio


async def main():
    # Experiment configuration

    with open(sys.argv[1]) as file:
        os.environ.update(json.load(file))
    openai.api_key = os.environ["OPENAI_API_KEY"]

    # Model and prompt

    llm = OpenAI(model=os.environ["LLM_NAME"], temperature=0.0)

    prompt = PromptTemplate(
            "Answer the query.\n"
            "Query: {query_str}\n"
            "Answer: "
            )

    # Load dataset

    dataset = pd.read_json(os.environ["DATASET"])

    # Retrieve

    queries = dataset["question"].to_list()

    tasks = [
            llm.apredict(prompt, query_str=query)
            for query in queries
            ]
    responses = await tqdm_asyncio.gather(*tasks)

    dataset["response"] = [response for response in responses]

    # Save results

    output_dir = Path("generations")
    file_name = "non_aug.json"
    output_file = output_dir / file_name

    os.makedirs(output_dir, exist_ok=True)

    dataset.to_json(
            output_file,
            orient="records",
            force_ascii=False,
            indent=4,
            )


if __name__ == "__main__":
    asyncio.run(main())
