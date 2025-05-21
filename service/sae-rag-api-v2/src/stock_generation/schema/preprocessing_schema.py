from pydantic import BaseModel, Field
from .base_schema import StockGenRequestDto


class PreprocessingFlowState(BaseModel):
    state_id: str = Field(..., min_length=1)
    request_dto: StockGenRequestDto
    route: str
    preprocessed_title: str
    preprocessed_url: str
    preprocessed_content: str
