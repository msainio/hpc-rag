#!/usr/bin/env python3

import json
import os
from pathlib import Path


def main():
    with open("./data/processed/curated.json") as file:
        old_pairs = json.load(file)

    new_pairs = []
    num_pairs_csc = 0
    num_pairs_lumi = 0

    for i, pair in enumerate(old_pairs):
        new_pairs.append(
                {
                    "idx": i,
                    "question": pair["question"][0],
                    "answer": pair["answer"][0],
                    "source": pair["source"],
                    }
                )

        if pair["source"].startswith("csc"):
            num_pairs_csc += 1
        elif pair["source"].startswith("lumi"):
            num_pairs_lumi += 1
        else:
            raise RuntimeError(f"Unknown data source: '{source}'")

    # Print summary
    print(f"{'CSC':<5}\t{num_pairs_csc:>5}")
    print(f"{'LUMI':<5}\t{num_pairs_lumi:>5}")
    print("-" * 13)
    print(f"{'Total':<5}\t{len(new_pairs):>5}")

    # Write to file
    output_dir = Path("./csc-services-qa/")
    os.makedirs(output_dir, exist_ok=True)
    output_file = output_dir / "csc_services_qa.json"
    
    with open(output_file, "w") as file:
        json.dump(new_pairs, file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    main()
