import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("AI-Middleware")


def log_ai_call(prompt, latency, cached):
    logger.info({
        "event": "ai_call",
        "latency_ms": latency,
        "cached": cached,
        "prompt_size": len(prompt)
    })
