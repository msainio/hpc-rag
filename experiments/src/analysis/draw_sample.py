#!/usr/bin/env python3

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

from utils import read_scores


def get_response(df, name, idx):
    df = df.copy()
    df["scores"] = df.apply(
            lambda x: {
                "bleu": x["bleu"],
                "rougeLsum": x["rougeLsum"],
                "meteor": x["meteor"],
                "bert_score": x["bert_score"],
                "bart_score_F": np.exp(x["bart_score"]["F"]),
                "entailment_F": x["entailment_score"]["F"],
                "sim_ref_hyp_F": x["sim_ref_hyp"]["F"],
                },
            axis=1,
            )
    if "source_nodes" in df.columns:
        df["source_nodes"] = df["source_nodes"].map(
                lambda x: [y["file_path"] for y in x]
                )
    columns = (
            {
                "bleu", "rougeLsum", "meteor",
                "bert_score", "bart_score", "entailment_score",
                "sim_ref_hyp", "sim_docs_ref", "sim_docs_hyp",
                }
            & set(df.columns)
            )
    df = df.drop(columns=columns)
    df = df.rename(
            columns={
                "response": name + "_response",
                "scores": name + "_scores",
                "source_nodes": name + "_nodes",
                }
            )
    return df.iloc[idx]


def get_sample(idx, gens):
    return pd.concat(
            [
                get_response(gens["vanilla"], "vanilla", idx),
                get_response(gens["baseline"], "baseline", idx),
                get_response(gens["best"], "best", idx),
                ]
            ).drop_duplicates()


def main():
    vanilla_scores = read_scores(
            "grouped-scores/augmentation/No Augmentation.json",
            include_length=False,
            include_retrieval=False,
            )
    baseline_scores = read_scores(
            "grouped-scores/augmentation/Augmentation.json",
            include_length=False,
            include_retrieval=False,
            )
    best_scores = read_scores(
            "grouped-scores/number-of-passages/16.json",
            include_length=False,
            include_retrieval=False,
            )

    vanilla = pd.read_json(
            "grouped-scores/augmentation/No Augmentation.json",
            )
    baseline = pd.read_json(
            "grouped-scores/augmentation/Augmentation.json",
            )
    best = pd.read_json(
            "grouped-scores/number-of-passages/16.json",
            )
    gens = {
            "vanilla": vanilla,
            "baseline": baseline,
            "best": best,
            }

    indices = {
            "argmax_vanilla_base": (  # same as argmax_base
                StandardScaler().fit_transform(
                    np.abs(vanilla_scores - baseline_scores)
                    ).mean(axis=1)
                ),
            "argmax_base_best": (
                StandardScaler().fit_transform(
                    np.abs(baseline_scores - best_scores)
                    ).mean(axis=1)
                ),
            "argmin_base": (
                StandardScaler().fit_transform(
                    baseline_scores
                    ).mean(axis=1)
                ),
            }

    for k, v in indices.items():
        arr = v
        if "argmin" in k:
            sample = get_sample(arr.argmin(), gens)
            total_len = (
                    len(sample["vanilla_response"])
                    + len(sample["baseline_response"])
                    + len(sample["best_response"])
                    )
            while total_len >= 4580:
                arr = np.delete(arr, (arr.argmin()), axis=0)
                sample = get_sample(arr.argmin(), gens)
                total_len = (
                        len(sample["vanilla_response"])
                        + len(sample["baseline_response"])
                        + len(sample["best_response"])
                        )
            indices[k] = arr.argmin()
        elif "argmax" in k:
            sample = get_sample(arr.argmax(), gens)
            total_len = (
                    len(sample["vanilla_response"])
                    + len(sample["baseline_response"])
                    + len(sample["best_response"])
                    )
            while total_len >= 4580:
                arr = np.delete(arr, (arr.argmax()), axis=0)
                sample = get_sample(arr.argmax(), gens)
                total_len = (
                        len(sample["vanilla_response"])
                        + len(sample["baseline_response"])
                        + len(sample["best_response"])
                        )
            indices[k] = arr.argmax()

    scores = {}

    for idx in indices.values():
        sample = get_sample(idx, gens)
        total_len = (
                len(sample["vanilla_response"])
                + len(sample["baseline_response"])
                + len(sample["best_response"])
                )
        print(f"{total_len=}")
        for k, v in sample.items():
            if "response" in k:
                print(k + ": " + repr(v))
            else:
                print(k + ": " + str(v))
        scores[idx] = pd.DataFrame(
                {
                    "vanilla": sample["vanilla_scores"],
                    "baseline": sample["baseline_scores"],
                    "best": sample["best_scores"],
                    }
                ).T.multiply(100).round(2)
        print()

    print(pd.concat(scores).to_latex(float_format="%.2f"))


if __name__ == "__main__":
    main()
