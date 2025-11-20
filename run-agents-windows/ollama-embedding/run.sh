#!/bin/bash


docker pull ollama/ollama

docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama

docker exec ollama ollama pull bge-m3:567m-fp16