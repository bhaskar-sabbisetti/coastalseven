from fastapi import APIRouter, Request, HTTPException
from schemas.ai_response import AIExplainResponse
from ai.middleware import ai_service

MODELS = {
    "fast": "facebook/bart-large-cnn",
    "balanced": "google/flan-t5-base",
    "quality": "google/flan-t5-large"
}

router = APIRouter(prefix="/ai", tags=["AI"])


@router.post("/route", response_model=AIExplainResponse)
def route_explain(
    topic: str,
    priority: str = "balanced",
    request: Request = None
):
    if priority not in MODELS:
        priority = "balanced"

    model_name = MODELS[priority]
    client_id = request.client.host

    prompt = f"Explain the topic clearly: {topic}"

    result = ai_service(
        prompt=prompt,
        client_id=client_id,
        model_name=model_name
    )

    if not result.get("success"):
        raise HTTPException(status_code=500, detail=result["error"])

    text = result["text"].strip()

    words = len(text.split())
    complexity = "low" if words < 60 else "medium" if words < 150 else "high"

    return AIExplainResponse(
        explanation=text,
        complexity=complexity
    )
