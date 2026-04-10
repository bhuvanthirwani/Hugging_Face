# Deploying LLMs for Free: The Hugging Face Guide

Stop paying for LLM API credits for your side projects! 🚀

Did you know Hugging Face offers a free hardware tier that is powerful enough to run production-grade LLMs? You get **2 vCPUs and 16GB of RAM** for free, allowing you to deploy models like **Llama 3** and integrate them directly into your applications.

## Why this is a win:

*   **Zero Cost:** No more OpenAI or Anthropic bills for personal testing.
*   **Full Control:** Deploy any model from the Hugging Face Hub (GGUF or AWQ formats work best on CPU).
*   **API Integration:** Use the Gradio-client or simple requests to call your model from any Python app.
*   **Privacy:** If you set your Space to private, your data stays within your account (requires a HF Token).

---

## Getting Started

To use the OLLAMA server deployed on Hugging Face, follow these steps:

### 1. Setup your Hugging Face space
*   Create a new Space on Hugging Face.
*   Use the `Dockerfile` provided in this directory to build your OLLAMA server.
*   The `Dockerfile` pre-pulls `llama3.2:1b-instruct-q4_K_M` for fast startup.

### 2. Configure Environment
In [sample_code.py](file:///c:/Projects/Hugging_Face/Ollama_LLM/sample_code.py), you need to set two variables:

*   **HF_TOKEN**: Your Hugging Face access token (found in Settings -> Access Tokens). Required if your Space is private.
*   **base_url**: Set this to your Space's direct URL. It usually looks like `https://user-space.hf.space`.

```python
# In sample_code.py
HF_TOKEN = "your_hf_token_here"

llm = ChatOllama(
    model="llama3.2:1b-instruct-q4_K_M",
    base_url="https://YOUR_HF_SPACE_URL.hf.space",
    # ...
)
```

### 3. Run the Sample Code
The sample code demonstrates how to use LangChain with Ollama for structured output (JSON).
```bash
python sample_code.py
```

---

## About Me

I am a developer focused on building efficient, cost-effective AI solutions. This project explores the potential of free hosting tiers (like Hugging Face Spaces) to run production-grade LLMs using OLLAMA, making AI more accessible for side projects and experimentation.
