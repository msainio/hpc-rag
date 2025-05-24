# Experiments

This directory contains code for running the experiments detailed in the
thesis.

## Replication

The `./config/baseline.json` file contains the configuration for
running the experiment pipeline for the baseline system. In order to build and
evaluate this system, follow these steps:

1. Prepare the HPC documentation knowledge base by running `bash ./scripts/get-knowledge-base.sh`.
2. Start the Qdrant vector store by running `sudo bash
   ./scripts/run-qdrant.sh`. The vector store is run a Docker container, so
   Docker Engine needs to be installed.
3. Change the value for `OPENAI_API_KEY` in the configuration file into a
   valid OpenAI API key.
4. Run `bash ./scripts/run-pipeline.sh ./config/baseline.json`.
5. For comparing the baseline system against the non-augmented LLM, evaluate
   the LLM by running `bash ./scripts/run-non-aug.sh ./config/baseline.json`.
   Any configuration file may be used for this, as long as it contains a valid
   OpenAI API key.

## Analysis

The code used for producing the tables and figures in the thesis are provided
in `./src/analysis/`, though these rely on having the score files stored under
`./grouped-scores/` using a specific naming scheme. Regardless, the plots
(but not the tables) produced using these these scripts are provided in
`./results/`.
