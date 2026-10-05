# FirstAgent

My first agent.

## Author

Ahmed Sadek

## Local LLM chat

Runs Qwen2.5-1.5B-Instruct (Q4 GGUF) on CPU via llama.cpp, with a streaming chat page.

    python3 -m venv .venv && . .venv/bin/activate
    pip install llama-cpp-python fastapi uvicorn huggingface_hub
    python -c "from huggingface_hub import hf_hub_download as d; d('Qwen/Qwen2.5-1.5B-Instruct-GGUF','qwen2.5-1.5b-instruct-q4_k_m.gguf',local_dir='models')"
    ./run.sh   # then open http://localhost:8000

Set `MODEL_PATH` to use a different GGUF model.
