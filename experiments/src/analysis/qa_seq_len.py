#!/usr/bin/env python3

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import spacy


def main():
    """Plot histograms of dataset text lengths.
    """
    df = pd.read_json("data/csc-services-qa/csc_services_qa.json")
    df.set_index("idx", inplace=True)

    nlp = spacy.load("en_core_web_sm")

    df["q_len"] = [len(x) for x in nlp.pipe(df["question"])]
    df["a_len"] = [len(x) for x in nlp.pipe(df["answer"])]
    df["data_source"] = df["source"].map(
            lambda x: "CSC" if "csc" in x else "LUMI"
            )

    df_csc = df[df["data_source"] == "CSC"]
    df_lumi = df[df["data_source"] == "LUMI"]

    sns.set_theme(
            rc={"figure.figsize":(16, 12)}
            )
    sns.set_color_codes()
    
    fig, axs = plt.subplots(2, 2)
    plt.subplots_adjust(hspace = 0.5)

    g1 = sns.histplot(
            df_csc, x="q_len", binwidth=5, binrange=(0, 160), ax=axs[0, 0],
            )
    g3 = sns.histplot(
            df_lumi, x="q_len", binwidth=5, binrange=(0, 160), ax=axs[0, 1],
            )
    g2 = sns.histplot(
            df_csc, x="a_len", binwidth=10, binrange=(0, 320), ax=axs[1, 0],
            )
    g4 = sns.histplot(
            df_lumi, x="a_len", binwidth=10, binrange=(0, 320), ax=axs[1, 1],
            )

    g1.set(
            xlabel="Words", xlim=(-10,170), ylim=(0,30),
            title=(
                "CSC Question Length "
                f"(M={np.round(df_csc['q_len'].mean(), 2)})"
                ),
            )
    g3.set(
            xlabel="Words", ylabel="", xlim=(-10,170), ylim=(0,30),
            title=(
                "LUMI Question Length "
                f"(M={np.round(df_lumi['q_len'].mean(), 2)})"
                ),
            )
    g2.set(
            xlabel="Words", xlim=(-20,340), ylim=(0,30),
            title=(
                "CSC Answer Length "
                f"(M={np.round(df_csc['a_len'].mean(), 2)})"
                ),
            )
    g4.set(
            xlabel="Words", ylabel="", xlim=(-20,340), ylim=(0,30),
            title=(
                "LUMI Answer Length "
                f"(M={np.round(df_lumi['a_len'].mean(), 2)})"
                ),
            )

    g1.set_xticks(range(0, 180, 20))
    g3.set_xticks(range(0, 180, 20))
    g2.set_xticks(range(0, 340, 40))
    g4.set_xticks(range(0, 340, 40))

    plt.savefig("results/qa_seq_len.png")
    plt.show()


if __name__ == "__main__":
    main()
