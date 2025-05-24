#!/bin/bash

# Run experimental pipeline. Provide the path to
# the configuration file as a command-line argument.

config=$1

python3 ./src/build_indices.py $config \
    && python3 ./src/run_queries.py $config \
    && python3 ./src/evaluate.py $config
