#!/bin/bash


git clone https://github.com/assafelovic/gpt-researcher.git

cp .env ./gpt-researcher/
rm ./gpt-researcher/requirements.txt
cp requirements.txt ./gpt-researcher/

