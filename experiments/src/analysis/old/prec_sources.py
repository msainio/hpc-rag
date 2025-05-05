#!/usr/bin/env python3

from matplotlib import pyplot as plt
import numpy as np
import os
import pandas as pd
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

    return pd.concat(data)


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
    for question_source in "csc", "lumi":
        for dirname, label in dirnames:
            if "augmentation" in dirname:
                df = read_dir(
                        dirname, label, metrics[:-2], False, question_source
                        )
            else:
                df = read_dir(dirname, label, metrics, True, question_source)
            df["source"] = question_source.upper()
            data.append(df)

    df_all = pd.concat(data)
    df_corr = df_all.groupby("source").corr("spearman")

    xyz = df_all.loc[df_all["source"] == "CSC"]

    prec_sources = pd.DataFrame(df_corr["Precision"])
    prec_sources["metric"] = [x[1] for x in prec_sources.index]
    prec_sources["source"] = [x[0] for x in prec_sources.index]

    prec_sources.index = range(len(prec_sources))
    prec_sources = prec_sources.loc[prec_sources["metric"] != "Precision"]

    sns.set_theme()

    fig, axs = plt.subplots(3, 3)

    #prec_csc.loc[prec_sources["source"] != "CSC"]
    #prec_lumi.loc[prec_sources["source"] != "LUMI"]

    xyz = xyz.reset_index()

    c = 0
    for i in range(3):
        for j in range(3):
            sns.scatterplot(data=xyz.iloc[:300], x=metrics[c], y="Precision", ax=axs[i][j])
            #sns.scatterplot(prec_lumi[metrics[c]], ax=axs[i][j])
            c += 1
            if c == 9:
                break

    #g = sns.catplot(prec_sources, x="metric", y="Precision",  hue="source",
    #        kind="bar",
    #        height=9,# aspect=1.33,
    #        )
    #g._legend.remove()
    #plt.legend()

    #plt.xlabel("")
    #plt.ylabel(r"$\rho$")

    #plt.savefig("results/prec_sources.png")
    plt.show()


if __name__ == "__main__":
    main()
