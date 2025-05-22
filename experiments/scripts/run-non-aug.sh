#!/bin/bash

config="./config/baseline.json"

python3 ./src/non-aug/generate.py $config \
    && python3 ./src/non-aug/evaluate.py $config
