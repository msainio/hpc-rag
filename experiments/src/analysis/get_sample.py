#!/usr/bin/env python3

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import spacy

from utils import read_scores


def get_response(df, name, idx):
    """Get the scores and texts for a system response.
    """
    df = df.copy()

    # Gather scores into one dictionary

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

    # Cross-system proportion

    if "source_nodes" in df.columns:
        df["cross_sys_prop"] = df.apply(
                lambda x: sum(
                    [
                        x["source"].split("-")[0] in y["file_path"].split("/")[2]
                        for y in x["source_nodes"]
                        ]
                    ) / len(x["source_nodes"]),
                axis=1,
                )
        df["scores"] = df.apply(
                lambda x: (
                    x["scores"] | {"cross_sys_prop": x["cross_sys_prop"]}
                    ),
                axis=1,
                )
        df["source_nodes"] = df["source_nodes"].map(
                lambda x: [y["file_path"] for y in x]
                )

    # Length ratio

    nlp = spacy.load("en_core_web_sm", enable=["tok2vec"])
    hyp_len = np.array([len(doc) for doc in nlp.pipe(df["response"])])
    ref_len = np.array([len(doc) for doc in nlp.pipe(df["answer"])])
    df["length_ratio"] = hyp_len / ref_len


    df["scores"] = df.apply(
            lambda x: (
                x["scores"] | {"length_ratio": x["length_ratio"]}
                ),
            axis=1,
            )

    # Drop columns that do not hold score dict or system outputs

    columns = (
            {
                "bleu", "rougeLsum", "meteor",
                "bert_score", "bart_score", "entailment_score",
                "sim_ref_hyp", "sim_docs_ref", "sim_docs_hyp",
                "cross_sys_prop", "length_ratio",
                }
            & set(df.columns)
            )
    df = df.drop(columns=columns)

    # Give columns system-specific names
    
    df = df.rename(
            columns={
                "response": name + "_response",
                "scores": name + "_scores",
                "source_nodes": name + "_nodes",
                }
            )

    return df.iloc[idx]


def get_sample(idx, gens):
    """Get the system responses and scores for a QA pair.
    """
    return pd.concat(
            [
                get_response(gens["vanilla"], "vanilla", idx),
                get_response(gens["baseline"], "baseline", idx),
                get_response(gens["best"], "best", idx),
                ]
            ).drop_duplicates()


def main():
    """Get representative samples from evaluation results.
    """

    # Get scores for systems

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

    # Compute aggregate scores

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

    # Get response texts

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

    # Drop QA pairs that are too long for displaying in report

    excluded = {}  # Store long QA pairs

    for k, v in indices.items():
        # Iteratively QA pairs with the desired properties until
        # the desired total response length is met
        arr = v
        if "argmin" in k:
            sample = get_sample(arr.argmin(), gens)
            total_len = (
                    len(sample["vanilla_response"])
                    + len(sample["baseline_response"])
                    + len(sample["best_response"])
                    )
            while total_len >= 4580:
                excluded[f"{k}_{len(excluded)}"] = arr.argmin()
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
                excluded[f"{k}_{len(excluded)}"] = arr.argmax()
                arr = np.delete(arr, (arr.argmax()), axis=0)
                sample = get_sample(arr.argmax(), gens)
                total_len = (
                        len(sample["vanilla_response"])
                        + len(sample["baseline_response"])
                        + len(sample["best_response"])
                        )
            indices[k] = arr.argmax()

    # Format and print QA pairs

    for d, name in [(indices, "Included"), (excluded, "Excluded")]:
        scores = {}
        print(name)

        for idx in d.values():
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
        print()


if __name__ == "__main__":
    main()
