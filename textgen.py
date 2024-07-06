import os
from dotenv import load_dotenv

import requests

# NOTE: define HF_TOKEN env variable
# ensure that token has appropriate permissions
load_dotenv()

HF_TOKEN = os.getenv('HF_TOKEN')

### BOILERPLATE

API_URL = "https://api-inference.huggingface.co/models/gpt2"
headers = {"Authorization": f"Bearer {HF_TOKEN}"}
def query(payload):
    """Standard query request"""
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

### END BOILERPLATE

def generate(prompt: str, *, 
    max_new_tokens: int = 50, 
    num_return_sequences: int = 1, 
    temperature: float = 0.8
) -> list[str]:
    """Send a text generation prompt with given parameters. Return the generated text(s)"""
    res = query({
        "inputs": prompt,
        "parameters": {
            "temperature": temperature,
            "max_new_tokens": max_new_tokens,
            "num_return_sequences": num_return_sequences
        }
    })

    return [text.get('generated_text') for text in res]


if __name__ == "__main__":
    prompt = "Life is a box of"
    res = generate("Life is a box of", max_new_tokens=50, num_return_sequences=1, temperature=0.8)

    print(f"Input: {prompt}\nGenerated Text: {res[0]}")