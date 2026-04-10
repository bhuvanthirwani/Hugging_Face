import time
from langchain_ollama import ChatOllama
from pydantic import BaseModel, Field

HF_TOKEN = ""

# 1. Define your schema
class QuickResponse(BaseModel):
    summary: str = Field(description="A 5-word summary")
    sentiment: str = Field(description="Positive or Negative")
    speed_test: float = Field(description="A random float for testing")

# 2. Initialize the model
llm = ChatOllama(
    model="llama3.2:1b-instruct-q4_K_M",
    base_url="https://YOUR_HF_SPACE_URL.hf.space",
    format="json",
    temperature=0,
    client_kwargs={
        "headers": {
            "Authorization": "Bearer {HF_TOKEN}",
            "Content-Type": "application/json"
        },
        "timeout": 60.0 # Llama 1B is so fast, 60s is plenty
    }
)

# Bind the schema
structured_llm = llm.with_structured_output(QuickResponse, method="json_schema")

# 3. Batch Loop
for i in range(1, 11):
    print(f"Call {i}/10...")
    start_time = time.time()
    
    try:
        res = structured_llm.invoke(f"The quick brown fox jumps over the lazy dog in iteration {i}.")
        end_time = time.time()
        
        print(f"Done in {end_time - start_time:.2f}s")
        print(res.model_dump_json(indent=2))
        
    except Exception as e:
        print(f"Failed: {e}")
    
    if i < 10:
        time.sleep(5)