import requests
import os
from dotenv import load_dotenv
load_dotenv()
HF_API_KEY = os.getenv("HF_API_KEY")

API_URL = "https://router.huggingface.co/hf-inference/models/facebook/bart-large-cnn"

headers = {
    "Authorization": f"Bearer {HF_API_KEY}",
    "Content-Type": "application/json"
}
prompt=input("enter your text:")
payload = {
    "inputs": f"{prompt}"
}

response = requests.post(API_URL, headers=headers, json=payload)

print("Status Code:", response.status_code)
print("Response:", response.json())
