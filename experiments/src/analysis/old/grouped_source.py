#!/usr/bin/env python3

from matplotlib import pyplot as plt
import numpy as np
import os
import pandas as pd
import seaborn as sns

from utils import read_scores


def read_dir(dirname, keys, question_source="both", include_length=True):
    # Set index labels
    if "embedding-model" in dirname:
        data = {"Small": None, "Large": None}
    elif "search-type" in dirname:
        data = {
                "Semantic": None, "BM25": None,
                "Hybrid, k=2": None, "Hybrid, k=4": None,
                "Hybrid, k=8": None, "Hybrid, k=16": None,
                }
    elif "re-ranking" in dirname:
        data = {
                "No Re-ranking": None, "Re-ranking, k=2": None,
                "Re-ranking, k=4": None, "Re-ranking, k=8": None,
                "Re-ranking, k=16": None,
                }
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
                    question_source,
                    include_length,
                    )
            data[key] = df.mean()

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
    metrics = [
            "BLEU", "ROUGE-L", "METEOR", "BERTScore", "BARTScore",
            "NLI", "SBERT-G",
            "Length",
            "SBERT-D", "Precision",
            ]

    data_both = []
    for dirname, label in dirnames:
        df = read_dir(
                dirname,
                metrics,
                question_source="both",
                #include_length=False,
                )
        if "chunk-size" not in dirname:
            df = df.drop(index=[label])
        data_both.append(df)

    df_both = pd.DataFrame(
            {
                "CSC": pd.concat(data_both).mean(),
                "LUMI": pd.concat(data_both).mean(),
                }
            )

    data_grouped = []
    for question_source in "csc", "lumi":
        for dirname, label in dirnames:
            df = read_dir(
                    dirname,
                    metrics,
                    question_source,
                    #include_length=False,
                    )
            if "chunk-size" not in dirname:
                df = df.drop(index=[label])
            df["source"] = question_source.upper()
            data_grouped.append(df)
    df_grouped = pd.concat(data_grouped)

    df_mean = df_grouped.groupby("source").mean().T
    df_mean.columns.name = None
    df_std = df_grouped.groupby("source").std().T
    df_std.columns.name = None

    df_change = (df_mean - df_both) / df_both * 100

    df_change["metric"] = df_change.index
    df_change = df_change.melt(
            id_vars=["metric"],
            value_vars=["CSC", "LUMI"],
            )

    x_name = "Metric"
    y_name = "Difference, %"
    hue_name = ""

    df_change = df_change.rename(
            columns={
                "metric": x_name,
                "value": y_name,
                "variable": hue_name,
                }
            )

    fig = plt.figure(figsize=(10, 7.5))
    sns.set_theme()
    g = sns.barplot(df_change, x=x_name, y=y_name, hue=hue_name)

    plt.xticks(rotation=45)

    plt.savefig("results/grouped_source.png")
    plt.show()

    df_mean = np.round(df_mean * 100, 2).map(lambda x: f"{x:.2f}")
    df_std = np.round(df_std * 100, 2).map(lambda x: f"{x:.2f}")

    print((df_mean + "±" + df_std).T.to_latex())


if __name__ == "__main__":
    main()
