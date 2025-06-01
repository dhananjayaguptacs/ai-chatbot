#!/bin/bash

ollama serve &

sleep 10

ollama pull gemma3:1b

streamlit run app.py --server.port=8501 --server.address=0.0.0.0