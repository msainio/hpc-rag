#!/bin/bash

run_name=$(python3 -c 'from src.utils import get_run_name; get_run_name()')

python3 ./src/build_indices.py $run_name \
    && python3 ./src/run_queries.py $run_name \
    #&& python3 ./src/evaluate.py ./responses/"${run_name}.json" \
    #&& python3 ./src/summarize.py ./scores/"${run_name}.json"
