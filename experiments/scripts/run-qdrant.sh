docker run -p 6333:6333 -p 6334:6334 \
    -v $(pwd)/data/qdrant:/qdrant/storage:z \
    qdrant/qdrant
