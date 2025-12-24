import requests
import os
from dotenv import load_dotenv

load_dotenv()

HF_API_KEY = os.getenv("HF_API_KEY")

MODEL_NAME = "facebook/bart-large-cnn"
PROVIDER = "huggingface"

API_URL = f"https://router.huggingface.co/hf-inference/models/{MODEL_NAME}"

HEADERS = {
    "Authorization": f"Bearer {HF_API_KEY}",
    "Content-Type": "application/json"
}


def generate_summary(text: str) -> dict:
    """
    Generate a summary for given text using an LLM.

    Returns:
        {
            summary: str | None
            success: bool
            error: str | None
            provider: str
            model: str
        }
    """

    if not text or len(text.strip()) < 20:
        return {
            "summary": None,
            "success": False,
            "error": "Text too short for summarization",
            "provider": PROVIDER,
            "model": MODEL_NAME
        }

    payload = {"inputs": text}

    try:
        response = requests.post(API_URL, headers=HEADERS, json=payload, timeout=90)
    except requests.exceptions.RequestException as e:
        return {
            "summary": None,
            "success": False,
            "error": str(e),
            "provider": PROVIDER,
            "model": MODEL_NAME
        }

    if response.status_code != 200:
        return {
            "summary": None,
            "success": False,
            "error": f"HTTP {response.status_code}",
            "provider": PROVIDER,
            "model": MODEL_NAME
        }

    try:
        data = response.json()
        summary = data[0]["summary_text"]
    except Exception:
        return {
            "summary": None,
            "success": False,
            "error": "Invalid response format",
            "provider": PROVIDER,
            "model": MODEL_NAME
        }

    return {
        "summary": summary,
        "success": True,
        "error": None,
        "provider": PROVIDER,
        "model": MODEL_NAME
    }

def call_llm(prompt: str) -> dict:
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_length": 300
        }
    }

    try:
        response = requests.post(
            API_URL,
            headers=HEADERS,
            json=payload,
            timeout=90
        )
    except requests.exceptions.RequestException as e:
        return {"success": False, "error": str(e)}

    if response.status_code != 200:
        return {"success": False, "error": response.text}

    try:
        text = response.json()[0]["summary_text"]
    except Exception:
        return {"success": False, "error": "Invalid LLM response"}

    return {"success": True, "text": text}

def call_ai_model(prompt: str) -> dict:
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_length": 300
        }
    }

    try:
        response = requests.post(API_URL, headers=HEADERS, json=payload, timeout=90)
    except requests.exceptions.RequestException as e:
        return {
            "success": False,
            "text": None,
            "error": str(e),
            "provider": PROVIDER,
            "model": MODEL_NAME
        }

    if response.status_code != 200:
        return {
            "success": False,
            "text": None,
            "error": response.text,
            "provider": PROVIDER,
            "model": MODEL_NAME
        }

    try:
        text = response.json()[0]["summary_text"]
    except Exception:
        return {
            "success": False,
            "text": None,
            "error": "Invalid LLM response format",
            "provider": PROVIDER,
            "model": MODEL_NAME
        }

    return {
        "success": True,
        "text": text,
        "error": None,
        "provider": PROVIDER,
        "model": MODEL_NAME
    }
