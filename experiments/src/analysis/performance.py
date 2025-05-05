#!/usr/bin/env python3

from collections import defaultdict
from matplotlib import pyplot as plt
import numpy as np
import os
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import StandardScaler

from utils import read_scores


def read_dir(dirname, keys, include_retrieval=True):
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
            "NLI", "SBERT", "Precision", "Length",
            ]
    groups = [
            "Augmentation",
            "Chunk Size", "Chunk Overlap", "Embedding Model",
            "Search Type", "Re-ranking", "Number of Passages",
            ]

    data_all = defaultdict(dict)
    for i, (dirname, baseline) in enumerate(dirnames):
        if "augmentation" in dirname:
            data = read_dir(dirname, metrics[:-2] + metrics[-1:], False)
        else:
            data = read_dir(dirname, metrics, True)
            del data[baseline]
        data_all[groups[i]] = data

    df_mean = pd.concat(
            {
                k1: pd.DataFrame(
                    {k2: v2.mean() * 100 for k2, v2 in v1.items()}
                    ).T
                for k1, v1 in data_all.items()
                }
            )
    df_std = pd.concat(
            {
                k1: pd.DataFrame(
                    {k2: v2.std() * 100 for k2, v2 in v1.items()}
                    ).T
                for k1, v1 in data_all.items()
                }
            ).round(2)

    ser_len = df_mean["Length"]
    df_mean = df_mean.drop(columns=["Length"])
    df_mean["Length"] = ser_len

    # Min-max scaling

    df_scaled = df_mean.drop(columns=["Precision", "Length"])

    scaler = StandardScaler()
    df_scaled[df_scaled.columns] = scaler.fit_transform(df_scaled)

    scaled_mean = df_scaled.mean(axis=1)
    scaled_std = df_scaled.std(axis=1)

    df_scaled["M"] = scaled_mean
    df_scaled["SD"] = scaled_std
    df_scaled = df_scaled.sort_values("M", ascending=False)

    df_scaled.index = [
            ": ".join([x, y]).capitalize() for x, y in df_scaled.index
            ]

    print(df_scaled)
    print()

    df_scaled["M"] = df_scaled["M"].round(2).map(
            #lambda x: f"{x:.2f}"[1:] if x < 1 else f"{x:.2f}"
            lambda x: f"{x:.2f}"
            )
    df_scaled["SD"] = df_scaled["SD"].round(2).map(
            #lambda x: f"{x:.2f}"[1:] if x < 1 else f"{x:.2f}"
            lambda x: f"{x:.2f}"
            )
    
    print(
            (
                df_scaled["M"]
                + df_scaled["SD"].map(lambda x: "±" + x)
                ).to_latex()
            )
    print()

    # Plot

    fig = plt.figure(figsize=(10, 7.5))
    sns.set_theme()

    ser_noaug = df_mean.droplevel(0).loc["No Augmentation"]

    df_plot = df_mean.droplevel(0).loc[
            [
                "Augmentation",
                "16",
                ]
            ]

    df_plot = (df_plot - ser_noaug) / ser_noaug

    df_plot = df_plot.drop(columns=["Precision", "Length"])
    df_plot.index = [
            "Baseline",
            "Best",
            ]

    print(
            df_plot.loc["Best"] - df_plot.loc["Baseline"]
            > df_plot.loc["Baseline"]
            )
    print()

    df_plot[""] = df_plot.index
    df_plot = df_plot.melt(id_vars=[""])

    g = sns.barplot(df_plot, x="variable", y="value", hue="")

    g.set(xlabel="Metric", ylabel="Percent change")

    plt.savefig("results/performance.png")
    plt.show()

    # Results table

    df_mean = df_mean.round(2)
    df_mean = df_mean.map(lambda x: f"{x:.2f}")
    df_mean += df_std.map(lambda x: f"±{x:.2f}" if isinstance(x, float) else x)

    df_mean = df_mean.droplevel(0)

    print(df_mean.to_latex())


if __name__ == "__main__":
    main()
