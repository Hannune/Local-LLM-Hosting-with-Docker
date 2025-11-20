FROM nvidia-ubuntu22.04

RUN apt-get update && apt-get install -y nano git python3 python3-pip && rm -rf /var/lib/apt/lists/*

RUN pip install vllm hf_xet

COPY ./gptq_marlin.py /usr/local/lib/python3.10/dist-packages/vllm/model_executor/layers/quantization/gptq_marlin.py
