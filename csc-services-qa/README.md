# CSC Services Question Answering Dataset

This directory contains code for building a question answering dataset about
CSC and LUMI computing services.

## How to build dataset

1. Get the raw data files by running `./scripts/get-lumi-data.sh` and
   `./src/get_csc_data.py`. For retrieving the CSC Apr 2023 and Nov 2023
   Markdown documents, use the download links on their HackMD pages. The links
   to the pages are provided below. Save the files under
   `./data/raw/csc-enveff-20230412/` and `./data/raw/csc-enveff-20231128/`.
2. Extract QA pairs by running `./src/extract_pairs.py`.
3. Create a copy of `./data/processed/uncurated.json` named
   `./data/processed/curated.json` and curate the data.
4. Run `./src/postprocess_pairs.py` to postprocess the QA pairs. The final
   dataset is saved as `./csc-services-qa/csc_services_qa.json`.

## Data Sources

### CSC Computing Environment trainings

* [CSC Computing Environment (April, 2023)](https://hackmd.io/lccV7miXRdyTqoSXqmGSxw)
* [CSC Computing Environment (September, 2023)](https://hackmd.io/@CSCBioMaria/ByS0nTrTh)
* [CSC Computing Environment (November, 2023)](https://hackmd.io/Ms9qP6YSSU-Nq_aEdnZn3Q)
* [CSC Computing Environment (February, 2024)](https://hackmd.io/@CSCBioMaria/Bk00RUSdp#)
* [CSC Computing Environment, Part 1: Basics (April, 2024)](https://hackmd.io/@CSCBioMaria/enveffapril2024)
* [CSC Computing Environment, Part 2: Next steps (May, 2024)](https://hackmd.io/@CSCBioMaria/enveffmay2024)
* [CSC Computing Environment, Part 1: Basics (October, 2024)](https://hackmd.io/@CSCBioMaria/rkcTtCUaR)
* [CSC Computing Environment, Part 2: Next steps (November, 2024)](https://hackmd.io/@CSCBioMaria/part2Nov24)

### LUMI Supercomputer trainings

* [LUMI 1-day training (May, 2023)](https://github.com/Lumi-supercomputer/LUMI-training-materials/tree/main/docs/1day-20230509)
* [LUMI 1-day training (September, 2023)](https://github.com/Lumi-supercomputer/LUMI-training-materials/tree/main/docs/1day-20230921)
* [LUMI 1-day training (February, 2024)](https://github.com/Lumi-supercomputer/LUMI-training-materials/tree/main/docs/1day-20240208)
* [Supercomputing with LUMI (May, 2024)](https://github.com/Lumi-supercomputer/LUMI-training-materials/tree/main/docs/2day-20240502)
* [Supercomputing with LUMI (December, 2024)](https://github.com/Lumi-supercomputer/LUMI-training-materials/tree/main/docs/2day-20241210)
