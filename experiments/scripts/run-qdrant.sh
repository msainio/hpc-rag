#!/bin/bash

data_dir="$(pwd)/data/qdrant"
mkdir -p $data_dir

docker run -p 6333:6333 -p 6334:6334 \
    -v $data_dir:/qdrant/storage:z \
    qdrant/qdrant
