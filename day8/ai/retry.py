import time
from functools import wraps


def retry(max_retries=3, delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                result = func(*args, **kwargs)
                if result.get("success"):
                    return result
                time.sleep(delay)
            return result
        return wrapper
    return decorator
