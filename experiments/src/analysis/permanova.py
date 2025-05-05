#!/usr/bin/env python3

import numpy as np
import os
import pandas as pd
from scipy.spatial.distance import pdist
from skbio import DistanceMatrix
from skbio.stats.distance import permanova

from utils import read_scores


def read_dir(dirname, keys, question_source="both", include_length=True,
        include_retrieval=True,
        ):
    data = []
    for root, dirs, files in os.walk(dirname):
        for file in files:
            df = read_scores(
                    os.path.join(root, file),
                    question_source,
                    include_length=include_length,
                    include_retrieval=include_retrieval,
                    )
            df.columns = keys
            df["group"] = file.split(".")[0].lower().replace(" ", "_")
            data.append(df)

    return data


def main():
    dirnames = [
            "grouped-scores/augmentation",
            "grouped-scores/chunk-size",
            "grouped-scores/chunk-overlap",
            "grouped-scores/embedding-model",
            "grouped-scores/search-type",
            "grouped-scores/re-ranking",
            "grouped-scores/number-of-passages",
            ]
    metrics = [
            "BLEU", "ROUGE-L", "METEOR", "BERTScore",
            "BARTScore", "NLI", "SBERT",
            ]

    for dirname in dirnames:
        if "augmentation" in dirname:
            data = read_dir(
                    dirname, metrics,
                    include_length=False,
                    include_retrieval=False,
                    )
        else:
            data = read_dir(
                    dirname, metrics,
                    include_length=False,
                    include_retrieval=False,
                    )

        df = pd.concat(data).reset_index(drop=True)
        dm = DistanceMatrix(
                pdist(df.select_dtypes("number"), metric="euclidean")
                )

        res = permanova(
                dm, df["group"].to_numpy(), permutations=99, seed=42
                )

        print(dirname)
        print(res)
        print()


if __name__ == "__main__":
    main()
