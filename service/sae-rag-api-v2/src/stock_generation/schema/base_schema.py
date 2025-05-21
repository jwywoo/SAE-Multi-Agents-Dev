from pydantic import BaseModel, Field
from typing import Optional, List
from .rag_schema import Stock


class StockGenRequestDto(BaseModel):
    original_title: str = Field(..., min_length=1)
    original_url: str = Field(..., min_length=5, max_length=2083)
    original_content: str = Field(..., min_length=1)


class StockGenResponseDto(BaseModel):
    state_id: str
    generated_stocks: list[Stock]


class FeedbackRequestDto(BaseModel):
    state_id: str = Field(..., min_length=1)
    feedback_score: int
