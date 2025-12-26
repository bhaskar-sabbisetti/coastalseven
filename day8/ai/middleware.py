import time
from ai.llm_client import call_ai_model
from ai.cache import get_cache_key, get_cached_response, set_cached_response
from ai.rate_limit import is_rate_limited
from ai.retry import retry
from ai.logger import log_ai_call
from ai.metrics import ai_requests_total, ai_latency_ms



@retry(max_retries=3)
def ai_service(prompt: str, client_id: str, model_name: str):

    if is_rate_limited(client_id):
        return {"success": False, "error": "Rate limit exceeded"}

    cache_key = get_cache_key(prompt, model_name)
    cached = get_cached_response(cache_key)

    if cached:
        log_ai_call(prompt, 0, True)
        return {
            "success": True,
            "text": cached,
            "model": model_name,
            "cached": True
        }

    start = time.time()
    result = call_ai_model(prompt, model_name)
    latency = int((time.time() - start) * 1000)

    log_ai_call(prompt, latency, False)

    if result.get("success"):
        set_cached_response(cache_key, result["text"])

    return result
