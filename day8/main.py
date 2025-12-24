from fastapi import FastAPI, Request, HTTPException
from ai.middleware import ai_service
from schemas.ai_response import AIExplainResponse
from ai.router import router as router

app = FastAPI(title="AI Backend with Redis Middleware")
app.include_router(router)


@app.post("/ai/summary", response_model=AIExplainResponse)
def explain_topic(topic: str, request: Request):

    prompt = f"Explain the topic clearly: {topic}"
    client_id = request.client.host

    result = ai_service(prompt, client_id)

    if not result.get("success"):
        raise HTTPException(status_code=429, detail=result["error"])

    text = result["text"].strip()

    word_count = len(text.split())
    if word_count < 60:
        complexity = "low"
    elif word_count < 150:
        complexity = "medium"
    else:
        complexity = "high"

    return AIExplainResponse(
        explanation=text,
        complexity=complexity
    )
