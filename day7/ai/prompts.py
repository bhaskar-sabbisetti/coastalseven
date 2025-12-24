EXPLAIN_CODE_PROMPT = """
You are a senior backend engineer.

Explain the following code and API specification clearly.

Cover:
- What the code does
- How the API works
- Important edge cases
- Possible improvements

Code:
{code}

API Specification:
{spec}
"""
SYSTEM_PROMPT = """
You are an API, not a chatbot.
Respond ONLY in valid JSON.
Response format:
{
  "explanation": "...",
  "complexity": "low | medium | high"
}
"""
