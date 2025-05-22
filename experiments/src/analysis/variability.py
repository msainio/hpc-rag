#!/usr/bin/env python3

from collections import defaultdict
from matplotlib import pyplot as plt
import numpy as np
import os
import pandas as pd
import seaborn as sns

from utils import read_scores


def read_dir(dirname, keys, include_length=True, include_retrieval=True):
    # Set index labels
    if "embedding-model" in dirname:
        data = {"Small": None, "Large": None}
    elif "search-type" in dirname:
        data = {"Semantic": None, "BM25": None, "Hybrid, k=2": None,
                "Hybrid, k=4": None, "Hybrid, k=8": None, "Hybrid, k=16": None}
    elif "re-ranking" in dirname:
        data = {"No Re-ranking": None, "Re-ranking, k=2": None, "Re-ranking, k=4": None,
                "Re-ranking, k=8": None, "Re-ranking, k=16": None}
    else:
        data = {}

    # Merge data
    for root, dirs, files in os.walk(dirname):
        for file in files:
            key = file.split(".")[0]
            if key.isdigit():
                key = int(key)
            df = read_scores(
                    os.path.join(root, file),
                    include_length=include_length,
                    include_retrieval=include_retrieval,
                    )
            df.columns = keys
            data[key] = df

    # Set index and columns
    alnum_indices = [
            "grouped-scores/embedding-model",
            "grouped-scores/search-type",
            "grouped-scores/re-ranking",
            ]
    if dirname not in alnum_indices:
        data = dict(sorted(data.items()))

    data = dict((str(k), v) for k, v in data.items())

    return data


def main():
    """Compute coefficients of variation for groups of systems.
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
    params = [
            "Augmentation", "Chunk size", "Chunk overlap", "Embedding model",
            "Search type", "Re-ranking", "Number of passages",
            ]
    metrics = [
            "BLEU", "ROUGE", "METEOR", "BERTScore",
            "BARTScore", "LogEq", "SemSim",
            ]

    data_all = defaultdict(dict)
    for dirname, baseline in dirnames:
        data = read_dir(
                dirname,
                metrics,
                include_length=False,
                include_retrieval=False,
                )
        data_all[dirname.split("/")[-1].split(".")[0]] = data

    df_mean = pd.concat(
            {
                k1: pd.DataFrame(
                    {k2: v2.mean() * 100 for k2, v2 in v1.items()}
                    ).T
                for k1, v1 in data_all.items()
                }
            )

    cvs = {}
    idx = df_mean.index.get_level_values(0).drop_duplicates()
    for i, key in enumerate(idx):
        df = df_mean.loc[key]
        cvs[params[i]] = df.std() / df.mean()

    df_cv = pd.DataFrame(cvs).T.round(2)
    df_cv["Mean"] = df_cv.mean(axis=1)

    print(df_cv.to_latex(float_format="%.2f"))


if __name__ == "__main__":
    main()
