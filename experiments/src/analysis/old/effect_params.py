#!/usr/bin/env python3

import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import os
import pandas as pd
import seaborn as sns

from utils import read_scores


def read_dir(
        dirname, keys, question_source="both", include_length=True,
        include_retrieval=True,
        ):
    # Set index labels
    if "embedding-model" in dirname:
        data = {"Small": None, "Large": None}
    elif "search-type" in dirname:
        data = {"Semantic": None, "BM25": None, "Hybrid, k=2": None,
                "Hybrid, k=4": None, "Hybrid, k=8": None,
                "Hybrid, k=16": None,
                }
    elif "re-ranking" in dirname:
        data = {
                "No Re-ranking": None, "Re-ranking, k=2": None,
                "Re-ranking, k=4": None, "Re-ranking, k=8": None,
                "Re-ranking, k=16": None,
                }
    else:
        data = {}

    # Merge series
    for root, dirs, files in os.walk(dirname):
        for file in files:
            key = file.split(".")[0]
            if key.isdigit():
                key = int(key)
            df = read_scores(
                    os.path.join(root, file),
                    question_source,
                    include_length,
                    include_retrieval,
                    ).mean()
            data[key] = df

    df_all = pd.DataFrame(data).T

    # Set index and columns
    alnum_indices = [
            "grouped-scores/embedding-model",
            "grouped-scores/search-type",
            "grouped-scores/re-ranking",
            ]
    if dirname not in alnum_indices:
        df_all = df_all.sort_index()

    df_all.index = [str(x) for x in df_all.index]
    df_all.columns = keys

    return df_all


def main():
    dirnames = [
            ("grouped-scores/chunk-size", "1024"),
            ("grouped-scores/chunk-overlap", "20"),
            ("grouped-scores/embedding-model", "Small"),
            ("grouped-scores/search-type", "Semantic"),
            ("grouped-scores/re-ranking", "No Re-ranking"),
            ("grouped-scores/number-of-passages", "2"),
            ]
    params = [
            "Chunk Size", "Chunk Overlap", "Embedding Model",
            "Search Type", "Re-ranking", "Number of Passages",
            ]
    metrics = [
            "BLEU", "ROUGE-L", "METEOR", "BERTScore",
            "BARTScore", "NLI", "SBERT-G",
            ]

    fig = plt.figure(figsize=(10, 7.5))
    sns.set_theme()

    df = read_dir(dirname, metrics, include_length=True)
    df_base = df.loc[baseline]
    
    df_diff = (((df - df_base) / df_base) * 100).T
    df_diff = df_diff.drop(baseline, axis=1)
    df_diff["metric"] = df_diff.index

    df_long = df_diff.melt(id_vars=["metric"], value_vars=df_diff.columns)

    x_name = "Metric"
    y_name = "Change, %"
    hue_name = ""

    df_long = df_long.rename(
            columns={
                "metric": x_name,
                "value": y_name,
                "variable": hue_name,
                }
            )

    g = sns.barplot(df_long, x=x_name, y=y_name, hue=hue_name, ax=axs[i])
    sns.move_legend(g, loc="lower left")

    plt.show()


if __name__ == "__main__":
    main()
