from pydantic import BaseModel, Field


class Stock(BaseModel):
    korean_name: str
    english_name: str
    market: str
    ticker_code: str


class RAGFlowState(BaseModel):
    state_id: str = Field(..., min_length=1)
    preprocessed_result: dict
    response_dto: list[Stock]
