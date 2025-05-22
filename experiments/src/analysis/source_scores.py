#!/usr/bin/env python3

import os
import pandas as pd

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
    """Create table of results grouped by question domain.
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
            "LogEq", "SemSim", "Precision", "Length Ratio",
            ]

    dataframes = {}

    for question_source in ["csc", "lumi"]:
        data = []
        for dirname, label in dirnames:
            if "augmentation" in dirname:
                data += read_dir(
                        dirname,
                        label,
                        metrics[:-2] + metrics[-1:],
                        question_source=question_source,
                        include_retrieval=False,
                        )
            else:
                data += read_dir(
                        dirname, label, metrics, question_source,
                        )

        df = pd.concat(data) * 100

        cols = list(df.columns)
        df_all = df[cols[:-2] + [cols[-1], cols[-2]]]

        df_mean = df_all.mean().round(2)
        df_mean = df_mean.map(lambda x: f"{x:.2f}")
        df_mean += df_all.std().map(
                lambda x: f"±{x:.2f}" if isinstance(x, float) else x
                )

        dataframes[question_source.upper()] = df_mean

    df_all = pd.DataFrame(dataframes)

    print(df_all.to_latex())


if __name__ == "__main__":
    main()
