import numpy as np
import pandas as pd
import spacy


def read_scores(
        score_file, question_source="both", include_length=True,
        include_retrieval=True,
        ):
    df = pd.read_json(score_file)
    df = df.set_index("idx")

    if question_source != "both":
        df = df[df["source"].str.contains(question_source)]

    # Generation metrics

    df["bart_score_F"] = df["bart_score"].map(lambda x: np.exp(x["F"]))
    df["entailment_F"] = df["entailment_score"].map(lambda x: x["F"])
    df["sim_ref_hyp_F"] = df["sim_ref_hyp"].map(lambda x: x["F"])

    # Retrieval metrics

    if include_retrieval:
        df["precision"] = df.apply(
                lambda x: sum(
                    [
                        x["source"].split("-")[0] in y["file_path"].split("/")[2]
                        for y in x["source_nodes"]
                        ]
                    ) / len(x["source_nodes"]),
                axis=1,
                )

    # Length

    if include_length:
        nlp = spacy.load("en_core_web_sm", enable=["tok2vec"])
        df["length"] = [len(doc) for doc in nlp.pipe(df["response"])]

    return df.select_dtypes("number")
