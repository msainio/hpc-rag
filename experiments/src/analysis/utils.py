import numpy as np
import pandas as pd
import spacy


def read_scores(
        score_file, question_source="both", include_length=True,
        include_retrieval=True,
        ):
    """Read scored evaluation results and return a dataframe.
    """
    df = pd.read_json(score_file)
    df = df.set_index("idx")

    if question_source != "both":
        df = df[df["source"].str.contains(question_source)]

    # Get F-measures for manually-computed metrics

    df["bart_score_F"] = df["bart_score"].map(lambda x: np.exp(x["F"]))
    df["entailment_F"] = df["entailment_score"].map(lambda x: x["F"])
    df["sim_ref_hyp_F"] = df["sim_ref_hyp"].map(lambda x: x["F"])

    # Retrieval precision

    if include_retrieval:
        df["cross_sys_prop"] = df.apply(
                lambda x: sum(
                    [
                        x["source"].split("-")[0] in y["file_path"].split("/")[2]
                        for y in x["source_nodes"]
                        ]
                    ) / len(x["source_nodes"]),
                axis=1,
                )

    # Response length ratio

    if include_length:
        nlp = spacy.load("en_core_web_sm", enable=["tok2vec"])
        hyp_len = np.array([len(doc) for doc in nlp.pipe(df["response"])])
        ref_len = np.array([len(doc) for doc in nlp.pipe(df["answer"])])
        df["length_ratio"] = hyp_len / ref_len

    return df.select_dtypes("number")
