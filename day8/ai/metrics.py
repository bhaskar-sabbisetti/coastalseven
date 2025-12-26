from prometheus_client import Counter, Histogram

ai_requests_total = Counter(
    "ai_requests_total",
    "Total AI requests"
)

ai_latency_ms = Histogram(
    "ai_latency_ms",
    "AI call latency (ms)"
)
