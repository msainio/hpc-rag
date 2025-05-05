#!/usr/bin/env python3

import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import os
import pandas as pd
import seaborn as sns

from utils import read_scores


def read_dir(dirname, keys):
    data = {}

    # Merge series
    for root, dirs, files in os.walk(dirname):
        for file in files:
            key = file.split(".")[0]
            if key.isdigit():
                key = int(key)
            df = read_scores(
                    os.path.join(root, file),
                    question_source="both",
                    #include_length=False,
                    include_retrieval=False,
                    )
            data[key] = df

    df_all = pd.concat(data)
    df_all.columns = keys

    return df_all


def main():
    sns.set_theme(
            rc={"figure.figsize": (10, 7.5)}
            )

    metrics = [
            "BLEU", "ROUGE-L", "METEOR", "BERTScore",
            "BARTScore", "NLI", "SBERT", "Length",
            ]

    df = read_dir("grouped-scores/augmentation", metrics)

    df_diff = (
            df.loc["Augmentation"].mean() - df.loc["No Augmentation"].mean()
            ) / df.loc["No Augmentation"].mean() * 100

    print(
            (df.loc["No Augmentation"].mean()*100).round(2).map(
                lambda x: f"{x:.2f}")
            + (df.loc["No Augmentation"].std()*100).round(2).map(
                lambda x: f"±{x:.2f}" if isinstance(x, float) else x)
            )

    g = sns.barplot(df_diff)
    g.set_ylabel("Relative change, %")
    g.set(title="Effect of Augmentation")

    plt.savefig("results/augmentation.png")
    plt.show()


if __name__ == "__main__":
    main()
