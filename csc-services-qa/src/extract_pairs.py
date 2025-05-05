#!/usr/bin/env python3

from collections import defaultdict
import json
import os
from pathlib import Path
import re


def get_patterns(file_name, source):
    if source.startswith("csc"):
        patterns = {
                "begin_qa": "## ✏️ Add your questions here",
                "end_qa": "##\s",
                "question": r"\s*-\s*\[?[\sx]?\]?\s*\**Q\d+:?\**(.*)\**",
                }
    elif source.startswith("lumi"):
        if re.match(r"A\d+_Misc_Questions", file_name):
            begin_qa = "# Miscellaneous questions"
        elif re.match(r"hedgedoc_notes", file_name):
            begin_qa = r"# Notes from the HedgeDoc page"
        elif re.match(r"notes_202[34]", file_name):
            begin_qa = "# Questions session"
        else:
            begin_qa = "## Q&A"
        patterns = {
                "begin_qa": begin_qa,
                "end_qa": None,
                "question": r"\d+\.\s*(.*)",
                }
    else:
        raise RuntimeError(f"Unknown data source: '{source}'")

    patterns.update(
            {
                "hyperlink": r"\!?\[([^\]]*)\]\([^\)]*\)",
                "stop": r"(##+|---)",
                }
            )
    return patterns


def get_pairs(file_path, source):
    in_qa_section = False
    patterns = get_patterns(file_path.name, source)
    qa_pair = {}
    qa_pairs = []
    res_end_qa = False

    with open(file_path) as file:
        for line in file:
            line = line.rstrip()
            line = re.sub(patterns["hyperlink"], r"\1", line)
            if not line:
                continue

            res_begin_qa = re.match(patterns["begin_qa"], line)
            if patterns["end_qa"]:
                res_end_qa = re.match(patterns["end_qa"], line)
            res_question = re.match(patterns["question"], line)
            res_stop = re.match(patterns["stop"], line)

            if res_begin_qa:
                in_qa_section = True
            elif in_qa_section and res_end_qa:
                if qa_pair:
                    if qa_pair["answer"]:
                        qa_pairs.append(qa_pair)
                    qa_pair = {}
                in_qa_section = False

            if not in_qa_section:
                continue

            if qa_pair and (res_question or res_stop):
                if qa_pair["answer"]:
                    qa_pairs.append(qa_pair)
                qa_pair = {}

            if res_question:
                qa_pair = {
                        "question": [],
                        "answer": [],
                        "source": source,
                        }
                qa_pair["question"].append(res_question.group(1).strip())
            elif qa_pair and line:
                qa_pair["answer"].append(line.removeprefix(" " * 4))

        if qa_pair and qa_pair["answer"]:
            qa_pairs.append(qa_pair)

    return qa_pairs


def index_pairs(all_pairs):
    indexed_pairs = []
    counts = defaultdict(int)

    for i, pair in enumerate(all_pairs):
        indexed_pair = {"idx": i}
        indexed_pair.update(
                {
                    "question": pair["question"],
                    "answer": pair["answer"],
                    "source": pair["source"],
                    }
                )
        indexed_pairs.append(indexed_pair)

        source = pair["source"]
        counts[source] += 1
        if source.startswith("csc"):
            counts["csc-total"] += 1
        elif source.startswith("lumi"):
            counts["lumi-total"] += 1
        else:
            raise RuntimeError("Unknown data source:", source)

    return indexed_pairs, counts


def main():
    input_dir = Path("./data/raw")
    input_files = input_dir.rglob("*.md")

    all_pairs = []
    counts = defaultdict(int)
    for input_file in input_files:
        source = input_file.parts[2]  # data/raw/(.*)
        qa_pairs = get_pairs(input_file, source)
        all_pairs.extend(qa_pairs)

    all_pairs = sorted(all_pairs, key=lambda x: x["source"])
    indexed_pairs, counts = index_pairs(all_pairs)

    for key in sorted(counts.keys(), key=lambda x: counts[x], reverse=True):
        if key not in {"csc-total", "lumi-total"}:
            print(f"{key:<25}{counts[key]:>5}")
    print("-" * 30)

    totals = ["csc-total", "lumi-total"]
    for key in sorted(totals, key=lambda x: counts[x], reverse=True):
        print(f"{key:<25}{counts[key]:>5}")
    print("-" * 30)

    print(f"{'Total':<25}{len(indexed_pairs):>5}")

    output_dir = "./data/processed/"
    os.makedirs(output_dir, exist_ok=True)
    output_file = output_dir + "uncurated.json"

    with open(output_file, "w") as file:
        json.dump(indexed_pairs, file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    main()
