from pydantic import BaseModel, Field, field_validator


class FeedbackFlowState(BaseModel):
    state_id: str = Field(..., min_length=1)
    feedback_score: int
    regeneration: bool
    preprocessed_result: dict = {}
    rag_result: dict = {}

    @field_validator("preprocessed_result", mode="before")
    @classmethod
    def default_if_none(cls, v):
        return v or {"Anonymous"}

    @field_validator("rag_result", mode="before")
    @classmethod
    def default_if_none(cls, v):
        return v or "Anonymous"
