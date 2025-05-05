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
                    include_retrieval=include_retrieval,
                    )
            df.columns = keys
            data.append(df)

    return data


def main():
    dirnames = [
            ("grouped-scores/augmentation", "Augmented"),
            ("grouped-scores/chunk-size", "1024"),
            ("grouped-scores/chunk-overlap", "20"),
            ("grouped-scores/embedding-model", "Small"),
            ("grouped-scores/search-type", "Semantic"),
            ("grouped-scores/re-ranking", "No Re-ranking"),
            ("grouped-scores/number-of-passages", "2"),
            ]
    metrics = [
            "BLEU", "ROUGE-L", "METEOR", "BERTScore", "BARTScore",
            "NLI", "SBERT", "Precision", "Length",
            ]

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
            data += read_dir(dirname, label, metrics)

    df_all = pd.concat(data)

    sns.set_theme()
    fig, axs = plt.subplots(1, 2, figsize=(12.5, 7.5))

    g1 = sns.histplot(
            df_all["Precision"], binwidth=0.05, binrange=[0, 1], ax=axs[0],
            )
    g2 = sns.histplot(
            df_all["Length"], binwidth=15, binrange=[0, 675], ax=axs[1],
            )

    #g1.set_xlabel("")
    #axs[0].set_title("Precision")
    #g2.set_xlabel("")
    #axs[1].set_title("Length")

    plt.savefig("results/histograms.png")
    plt.show()

    df_ranks = df_all.rank()
    matrix = []
    for x in df_ranks.columns:
        row = []
        for y in df_ranks.columns:
            res = spearmanr(df_ranks[x], df_ranks[y], nan_policy="omit")
            row.append(res.pvalue)
        matrix.append(row)

    df_matrix = pd.DataFrame(matrix, index=metrics, columns=metrics)

    df_star = np.where(df_matrix < 0.05, "\n*", "")
    df_star = np.where(df_matrix < 0.01, df_star + "*", df_star + "")
    df_star = np.where(df_matrix < 0.001, df_star + "*", df_star + "")

    df_corr = df_all.corr("spearman")

    # Average correlation

    df_tab = df_corr.copy()
    df_tab = df_tab.map(lambda x: np.nan if x == 1 else x)
    df_tab = (
            df_tab.mean().round(2).map(lambda x: f"{x:.2f}")
            + df_tab.std().round(2).map(lambda x: f"±{x:.2f}")
            )
    print(df_tab.to_latex())

    # Correlation matrix

    df_annot = df_corr.map(lambda x: f"{np.round(x, 2):.2f}")
    df_annot += df_star

    plt.figure(figsize=(12, 10))
    sns.set_theme()

    #annot = True
    annot = df_annot
    #fmt = ".2g"
    fmt = ""

    g = sns.heatmap(
            df_corr, annot=annot, vmin=-1, vmax=1, cmap="icefire", fmt=fmt,
            )
    g.xaxis.tick_top()
    plt.xticks(rotation=45)
    plt.yticks(rotation=0)

    plt.savefig("results/spearman.png")
    plt.show()


if __name__ == "__main__":
    main()
