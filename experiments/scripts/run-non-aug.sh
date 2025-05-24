#!/bin/bash

# Run experimental pipeline. Provide the path to a configuration file
# containing a valid OpenAI API key as a command-line argument.

config=$1

python3 ./src/non-aug/generate.py $config \
    && python3 ./src/non-aug/evaluate.py $config
