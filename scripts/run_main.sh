#!/bin/bash
set +x

export OPENAI_API_KEY=""

python src/main.py

bash scripts/build_md.sh