#!/usr/bin/env python3

import pandas as pd


def main():
    """Compare SDs of experimental results to those of Lyu et al. (2025):
    https://dl.acm.org/doi/abs/10.1145/3701228
    """
    crud_rag = {
            "bleu": [
                19.27, 20.23, 20.73, 21.05, 20.61,
                ],
            "rouge": [
                32.57, 34.21, 34.95, 35.04, 35.01,
                ],
            "bertscore": [
                85.65, 86.93, 87.66, 87.81, 88.02,
                ],
            }
    crud_rag = pd.DataFrame(crud_rag)

    print("CRUD-RAG")
    print(crud_rag.std())
    print()

    aug = {
            "bleu": [
                1.64, 2.51
                ],
            "rouge": [
                19.61, 23.64
                ],
            "bertscore": [
                8.60, 14.01
                ],
            }
    aug = pd.DataFrame(aug)

    print("Augmentation")
    print(aug.std())
    print()

    top_k = {
            "bleu": [
                2.51, 2.56, 2.67, 2.63,
                ],
            "rouge": [
                23.64, 23.83, 24.02, 24.18,
                ],
            "bertscore": [
                14.01, 14.21, 14.43, 14.94,
                ],
            }
    top_k = pd.DataFrame(top_k)

    print("Number of context passages")
    print(top_k.std())
    print()


if __name__ == "__main__":
    main()
