#!/usr/bin/env python3

from matplotlib import pyplot as plt
import numpy as np
import os
import pandas as pd
from scipy.stats import spearmanr
import seaborn as sns

from utils import read_scores


def read_dir(
        dirname, label, keys, question_source="both", include_length=True, 
        include_retrieval=True, 
        ):
    data = []
    for root, dirs, files in os.walk(dirname):
        for file in files:
            key = file.split(".")[0]
            if key.isdigit():
                key = int(key)
            if "chunk-size" not in dirname:
                if file.split(".")[0] == label:
                    continue
            df = read_scores(
                    os.path.join(root, file),
                    question_source,
                    include_length=include_length,
                    include_retrieval=include_retrieval,
                    )
            df.columns = keys
            data.append(df)

    return data


def main():
    """Plot histograms of evaluation metrics, precision and length ratio.
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
    metrics = [
            "BLEU", "ROUGE", "METEOR", "BERTScore", "BARTScore",
            "Log. Eq.", "Sem. Sim.", "Cross-Sys. Prop.", "Length Ratio",
            ]

    data_all = {}

    data = []
    for dirname, label in dirnames:
        if "augmentation" in dirname:
            data += read_dir(
                    dirname,
                    label,
                    metrics[:-2] + metrics[-1:],
                    include_retrieval=False,
                    )
        else:
            data += read_dir(
                    dirname, label, metrics,
                    )

    df_all = pd.concat(data) * 100

    # Plot histograms

    sns.set_theme()
    fig, axs = plt.subplots(3, 3, figsize=(14, 10.5))
    plt.subplots_adjust(hspace=0.4, wspace=0.3)

    c = 0
    for i in range(3):
        for j in range(3):
            label = df_all.columns[c]
            g = sns.histplot(
                    df_all[label],
                    ax=axs[i][j],
                    bins="fd",
                    binrange=np.percentile(df_all[label].dropna(), [1, 99]),
                    )
            g.set(xlabel=f"{label} (M={np.round(df_all[label].mean(), 2)})")
            if not j == 0:
                g.set(ylabel="")
            c += 1

    plt.savefig("results/histograms.png")
    plt.show()


if __name__ == "__main__":
    main()
