#!/usr/bin/env python3

from matplotlib import pyplot as plt
import numpy as np
import os
import pandas as pd
from scipy.stats import probplot
import seaborn as sns

from utils import read_scores


def read_dir(
        dirname, label, keys, include_retrieval=True, question_source="both",
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
                        include_retrieval,
                        question_source,
                        )
                df.columns = keys
                data.append(df)

    return data


def main():
    dirnames = [
            ("grouped-scores/augmentation", "Augmented"),
            ("grouped-scores/chunk-size", "1024"),
            ("grouped-scores/chunk-overlap", "20"),
            ("grouped-scores/embed", "Small"),
            ("grouped-scores/hybrid-search", "Vector"),
            ("grouped-scores/top-k", "2"),
            ("grouped-scores/rerank", "No rerank"),
            ]
    metrics = [
            "BLEU", "ROUGE-L", "METEOR", "BERTScore", "BARTScore",
            "NLI", "SBERT-G", "SBERT-D", "Precision",
            ]

    data = []

    for dirname, label in dirnames:
        if "augmentation" in dirname:
            data += read_dir(dirname, label, metrics[:-2], False)
        else:
            data += read_dir(dirname, label, metrics)

    sns.set_theme()

    for df in data:
        labels = list(df.columns)
        fig, axs = plt.subplots(3, 3)
        c = 0
        for i in range(3):
            for j in range(3):
                sns.histplot(df[labels[c]], ax=axs[i][j])
                #scipy.stats.probplot(df[labels[c]], plot=axs[i][j])
                c += 1
                if c > len(labels) - 1:
                    break
        plt.show()


if __name__ == "__main__":
    main()
