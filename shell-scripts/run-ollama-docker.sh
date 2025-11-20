#!/bin/bash

docker run -d --gpus all \
-v /your/ollama/path:/root/.ollama \
-p 11434:11434 \
--name server-ollama-3 \
-e OLLAMA_NUM_PARALLEL=1 \
-e OLLAMA_KEEP_ALIVE=-1h \
-e OLLAMA_CONTEXT_LENGTH=32768 \
ollama/ollama:0.12.5
