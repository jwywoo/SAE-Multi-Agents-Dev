from pydantic import BaseModel, Field
from typing import Optional, List


class RequestDto(BaseModel):
    original_title: str = Field(..., min_length=1)
    original_url: str = Field(..., min_length=5, max_length=2083)
    original_content: str = Field(..., min_length=1)


class Stock(BaseModel):
    korean_name: str
    english_name: str
    market: str
    ticker_code: str


class ResponseDto(BaseModel):
    generated_stocks: list[Stock]


class PreprocessingFlowState(BaseModel):
    route: str
    preprocessed_title: str
    preprocessed_url: str
    preprocessed_content: str


class RAGFlowState(BaseModel):
    route: str


class FlowState(BaseModel):
    request_dto: RequestDto
    generated_stocks: List[Stock]
    preprocessing_flow_state: PreprocessingFlowState
    rag_flow_state: RAGFlowState
