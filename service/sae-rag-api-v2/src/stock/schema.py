from pydantic import BaseModel, Field
from typing import Optional, List


class Stock(BaseModel):
    korean_name: str
    english_name: str
    market: str
    ticker_code: str


class StockGenRequestDto(BaseModel):
    original_title: str = Field(..., min_length=1)
    original_url: str = Field(..., min_length=5, max_length=2083)
    original_content: str = Field(..., min_length=1)


class ResponseDto(BaseModel):
    generated_stocks: list[Stock]


class PreprocessingFlowState(BaseModel):
    state_id: str = Field(..., min_length=1)
    request_dto: StockGenRequestDto
    route: str
    preprocessed_title: str
    preprocessed_url: str
    preprocessed_content: str


class RAGFlowState(BaseModel):
    state_id: str = Field(..., min_length=1)
    preprocessed_result: dict
    response_dto: list[Stock]


class FeedbackFlowState(BaseModel):
    state_id: str = Field(..., min_length=1)
    feedback_score: int
    regeneration: bool
    preprocessed_result: dict
    rag_result: dict
