#!/usr/bin/env python3

from bart_score import BARTScorer
from bert_score import BERTScorer
from datetime import datetime
from itertools import chain
from nltk.translate.meteor_score import single_meteor_score
import numpy as np
import os
import pandas as pd
from pathlib import Path
import re
from rouge_score import rouge_scorer
from sacrebleu.metrics import BLEU
from sentence_transformers import CrossEncoder, SentenceTransformer
import spacy
import sys
import torch
from tqdm import tqdm


def compute_entailment(srcs, tgts, model):
    all_scores = []

    for src in srcs:
        texts = [[src, tgt] for tgt in tgts]
        scores = model.predict(texts, show_progress_bar=False)
        all_scores.append(scores[:, 0])

    return np.max(all_scores, axis=0).mean()


def compute_similarity(refs, hyps, docs, model, top_k):
    all_ref_sents = []
    ref_sizes = []
    all_hyp_sents = []
    hyp_sizes = []

    for ref, hyp in zip(refs, hyps):
        ref_sents = [sent.text for sent in ref.sents]
        all_ref_sents.extend(ref_sents)
        ref_sizes.append(len(ref_sents))

        hyp_sents = [sent.text for sent in hyp.sents]
        all_hyp_sents.extend(hyp_sents)
        hyp_sizes.append(len(hyp_sents))

    all_doc_sents = []
    doc_sizes = []

    for doc in docs:
        doc_sents = [sent.text for sent in doc.sents]
        all_doc_sents.extend(doc_sents)
        doc_sizes.append(len(doc_sents))

    ref_chunks = model.encode(
            all_ref_sents,
            show_progress_bar=True,
            convert_to_tensor=True,
            ).split(ref_sizes)
    hyp_chunks = model.encode(
            all_hyp_sents,
            show_progress_bar=True,
            convert_to_tensor=True,
            ).split(hyp_sizes)

    all_doc_embeds = model.encode(
            all_doc_sents,
            show_progress_bar=True,
            convert_to_tensor=True,
            ).split(doc_sizes)
    doc_chunks = [
            all_doc_embeds[i : i + top_k]
            for i in range(0, len(all_doc_sents), top_k)
            ]

    iterator = zip(hyp_chunks, ref_chunks, doc_chunks)
    sim_ref_hyp = []
    sim_docs_hyp = []
    sim_docs_ref = []

    for ref_embeds, hyp_embeds, doc_chunk in iterator:
        scores_ref_hyp = model.similarity(ref_embeds, hyp_embeds).numpy()
        sim_ref_hyp_P = scores_ref_hyp.max(axis=0).mean()
        sim_ref_hyp_R = scores_ref_hyp.max(axis=1).mean()
        sim_ref_hyp_F = np.mean([sim_ref_hyp_P, sim_ref_hyp_R])
        sim_ref_hyp.append(
                {"P": sim_ref_hyp_P, "R": sim_ref_hyp_R, "F": sim_ref_hyp_F}
                )

        sim_docs_ref_single = []
        sim_docs_hyp_single = []

        for doc_embeds in doc_chunk:
            scores_doc_ref = model.similarity(doc_embeds, ref_embeds).numpy()
            sim_doc_ref_P = scores_doc_ref.max(axis=0).mean()
            sim_doc_ref_R = scores_doc_ref.max(axis=1).mean()
            sim_doc_ref_F = np.mean([sim_doc_ref_P, sim_doc_ref_R])
            sim_docs_ref_single.append(
                    {
                        "P": sim_doc_ref_P,
                        "R": sim_doc_ref_R,
                        "F": sim_doc_ref_F
                        }
                    )

            scores_doc_hyp = model.similarity(doc_embeds, hyp_embeds).numpy()
            sim_doc_hyp_P = scores_doc_hyp.max(axis=0).mean()
            sim_doc_hyp_R = scores_doc_hyp.max(axis=1).mean()
            sim_doc_hyp_F = np.mean([sim_doc_hyp_P, sim_doc_hyp_R])
            sim_docs_hyp_single.append(
                    {
                        "P": sim_doc_hyp_P,
                        "R": sim_doc_hyp_R,
                        "F": sim_doc_hyp_F
                        }
                    )

        sim_docs_ref.append(sim_docs_ref_single)
        sim_docs_hyp.append(sim_docs_hyp_single)

    return sim_ref_hyp, sim_docs_ref, sim_docs_hyp


def main():
    # Experiment configuration

    with open("config.json") as file:
        os.environ.update(json.load(file))

    run_name = (
            f"csc_{os.environ['CHUNK_SIZE']}_{os.environ['CHUNK_OVERLAP']}_"
            f"k{k}_m{m}_n{n}_{os.environ['RERANK_MODEL'].split('/')[-1]}"
            )

    # Read results file

    df = pd.read_json(f"./generations/{run_name}.json")

    # Prepare input texts

    nlp = spacy.load(
            "en_core_web_sm",
            exclude=["tagger", "ner", "lemmatizer", "textcat"])

    source_nodes = [
        node["content"] for node in
        chain.from_iterable(df["source_nodes"].to_list())
        ]

    refs = list(
            tqdm(nlp.pipe(df["answer"].to_list()),
                desc="Preparing references", total=df.shape[0])
            )
    hyps = list(
            tqdm(nlp.pipe(df["response"].to_list()),
                desc="Preparing hypotheses", total=df.shape[0])
            )
    docs = list(
            tqdm(iterable=nlp.pipe(source_nodes),
                desc="Preparing documents", total=len(source_nodes))
            )

    # Define metrics

    bleu = BLEU(effective_order=True)
    rouge = rouge_scorer.RougeScorer(["rougeLsum"], use_stemmer=True)
    bert_scorer = BERTScorer(model_type="microsoft/deberta-large-mnli",
            lang="en", rescale_with_baseline=True)
    bart_scorer = BARTScorer(
            device="cpu", checkpoint="facebook/bart-large-cnn")
    ent_model = CrossEncoder(
            "MoritzLaurer/DeBERTa-v3-large-mnli-fever-anli-ling-wanli",
            default_activation_function=torch.nn.Softmax(dim=1),
            tokenizer_args={"use_fast": False},
            )
    sim_model = SentenceTransformer("sentence-transformers/all-mpnet-base-v2")

    # Compute scores

    start = datetime.now()

    bleu_scores = [
            bleu.sentence_score(
                hypothesis=hyp.text, references=[ref.text]).score * 0.01
            for ref, hyp in tqdm(zip(refs, hyps),
                desc="Computing BLEU scores", total=len(refs))
            ]

    meteor_scores = [
            single_meteor_score(
                reference=[tok.text for tok in ref],
                hypothesis=[tok.text for tok in hyp]
                )
            for ref, hyp in tqdm(zip(refs, hyps),
                desc="Computing METEOR scores", total=len(refs))
            ]

    rouge_scores = [
            rouge.score(
                target="\n".join(
                    re.sub(r"\s+", " ", sent.text) for sent in ref.sents),
                prediction="\n".join(
                    re.sub(r"\s+", " ", sent.text) for sent in hyp.sents)
                )["rougeLsum"].fmeasure
            for ref, hyp in tqdm(zip(refs, hyps),
                desc="Computing ROUGE-L scores", total=len(refs))
            ]

    print("Computing BERTScores")
    bert_scores = bert_scorer.score(
            cands=[re.sub(r"\s+", " ", hyp.text) for hyp in hyps],
            refs=[re.sub(r"\s+", " ", ref.text) for ref in refs]
            )[2].numpy()

    print("Computing BARTScores (r -> h)")
    bart_scores_P = bart_scorer.score(
            srcs=[ref.text for ref in refs],
            tgts=[hyp.text for hyp in hyps]
            )
    print("Computing BARTScores (h -> r)")
    bart_scores_R = bart_scorer.score(
            srcs=[hyp.text for hyp in hyps],
            tgts=[ref.text for ref in refs]
            )
    bart_scores_F = np.mean([bart_scores_P, bart_scores_R], axis=0)
    bart_scores = [{"P": P, "R": R, "F": F}
            for P, R, F in zip(bart_scores_P, bart_scores_R, bart_scores_F)]

    entailment_P = [
            compute_entailment(
                srcs=[sent.text for sent in ref.sents],
                tgts=[sent.text for sent in hyp.sents],
                model=ent_model
                )
            for ref, hyp in tqdm(zip(refs, hyps),
                desc="Computing entailment scores (r -> h)", total=len(refs))
            ]
    entailment_R = [
            compute_entailment(
                srcs=[sent.text for sent in hyp.sents],
                tgts=[sent.text for sent in ref.sents],
                model=ent_model
                )
            for ref, hyp in tqdm(zip(refs, hyps),
                desc="Computing entailment scores (h -> r)", total=len(refs))
            ]
    entailment_F = np.mean([entailment_P, entailment_R], axis=0)
    entailment_scores = [{"P": P, "R": R, "F": F}
            for P, R, F in zip(entailment_P, entailment_R, entailment_F)]

    top_k = len(df["source_nodes"][0])
    sim_ref_hyp, sim_docs_ref, sim_docs_hyp = compute_similarity(
            refs, hyps, docs, sim_model, top_k)

    end = datetime.now()

    print(f"Evaluation finished in {end - start}")

    # Save results

    df["bleu"] = bleu_scores
    df["rougeLsum"] = rouge_scores
    df["meteor"] = meteor_scores
    df["bert_score"] = bert_scores
    df["bart_score"] = bart_scores
    df["entailment_score"] = entailment_scores
    df["sim_ref_hyp"] = sim_ref_hyp
    df["sim_docs_ref"] = sim_docs_ref
    df["sim_docs_hyp"] = sim_docs_hyp

    output_dir = Path("./scores")
    output_file = output_dir / f"{run_name}.json"

    os.makedirs(output_dir, exist_ok=True)

    df.to_json(
            output_file,
            orient="records",
            force_ascii=False,
            indent=4,
            )


if __name__ == "__main__":
    main()
