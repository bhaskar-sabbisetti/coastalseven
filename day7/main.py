from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from ai.llm_client import generate_summary,call_llm
from ai.prompts import EXPLAIN_CODE_PROMPT

app = FastAPI(
    title="AI Summarization API",
    description="FastAPI backend with Hugging Face LLM integration",
    version="1.0.0"
)
class ExplainRequest(BaseModel):
    code: str
    spec: str
class ExplainResponse(BaseModel):
    summary: str
    logic_explanation: str
    edge_cases: list[str]
    suggested_improvements: list[str]

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


@app.post("/ai/explain")
def explain_code(payload: ExplainRequest):
    prompt = EXPLAIN_CODE_PROMPT.format(
        code=payload.code,
        spec=payload.spec
    )

    llm_result = call_llm(prompt)

    if not llm_result["success"]:
        raise HTTPException(
            status_code=500,
            detail=llm_result["error"]
        )

    return {
        "explanation": llm_result["text"],
        "provider": "huggingface",
        "model": "facebook/bart-large-cnn"
    }
