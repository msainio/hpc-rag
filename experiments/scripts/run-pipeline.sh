#!/bin/bash

config="./config/baseline.json"

python3 ./src/build_indices.py $config \
    && python3 ./src/run_queries.py $config \
    && python3 ./src/evaluate.py $config
