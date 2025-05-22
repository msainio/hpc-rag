#!/usr/bin/env python3

from itertools import chain
import os
import pandas as pd

from utils import read_scores


def read_dir(dirname, label, domain):
    data = []
    for root, dirs, files in os.walk(dirname):
        for file in files:
            key = file.split(".")[0]
            if key.isdigit():
                key = int(key)
            if "chunk-size" not in dirname:
                if file.split(".")[0] == label:
                    continue

            df = pd.read_json(os.path.join(root, file))

            if domain != "total":
                df = df[df["source"].str.contains(domain)]

            ser = df["source_nodes"].map(
                    lambda x: [y["file_path"].split("/")[2] for y in x]
                    )
            data += list(chain.from_iterable(ser.to_list()))

    return data


def main():
    """Count number of document chunks retrieved from each data source.
    """
    dirnames = [
            ("grouped-scores/augmentation", "Augmentation"),
            ("grouped-scores/chunk-size", "1024"),
            ("grouped-scores/chunk-overlap", "20"),
            ("grouped-scores/embedding-model", "Small"),
            ("grouped-scores/search-type", "Semantic"),
            ("grouped-scores/re-ranking", "No Re-ranking"),
            ("grouped-scores/number-of-passages", "2"),
            ]

    all_data = {}

    for domain in ["csc", "lumi", "total"]:
        data = []
        for dirname, label in dirnames:
            if not "augmentation" in dirname:
                data += read_dir(dirname, label, domain)

        all_data[domain] = pd.Series(data).value_counts()

    print(pd.DataFrame(all_data).to_latex())


if __name__ == "__main__":
    main()
