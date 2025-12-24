import requests
import os
from dotenv import load_dotenv

load_dotenv()

HF_API_KEY = os.getenv("HF_API_KEY")
PROVIDER = "huggingface"

def call_ai_model(prompt: str, model_name: str) -> dict:
    api_url = f"https://router.huggingface.co/hf-inference/models/{model_name}"

    headers = {
        "Authorization": f"Bearer {HF_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_length": 300
        }
    }

    try:
        response = requests.post(api_url, headers=headers, json=payload, timeout=90)
    except requests.exceptions.RequestException as e:
        return {"success": False, "error": str(e)}

    if response.status_code != 200:
        return {"success": False, "error": response.text}

    try:
        data = response.json()
        text = data[0].get("summary_text") or data[0].get("generated_text")
    except Exception:
        return {"success": False, "error": "Invalid LLM response"}

    return {
        "success": True,
        "text": text,
        "model": model_name,
        "provider": PROVIDER
    }
