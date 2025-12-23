from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from ai.llm_client import generate_summary

app = FastAPI(
    title="AI Summarization API",
    description="FastAPI backend with Hugging Face LLM integration",
    version="1.0.0"
)

class SummarizeRequest(BaseModel):
    text: str

class SummarizeResponse(BaseModel):
    summary: str | None
    success: bool
    error: str | None
    provider: str
    model: str

@app.post("/ai/summarize", response_model=SummarizeResponse)
def summarize_text(payload: SummarizeRequest):
    result = generate_summary(payload.text)

    if not result["success"]:
        raise HTTPException(
            status_code=400,
            detail=result["error"]
        )

    return result
