from pydantic import BaseModel
from typing import Literal


class AIExplainResponse(BaseModel):
    explanation: str
    complexity: Literal["low", "medium", "high"]
