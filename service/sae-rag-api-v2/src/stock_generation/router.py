from fastapi import APIRouter, status
from .schema.base_schema import StockGenRequestDto, StockGenResponseDto, FeedbackRequestDto
from .service.generation_service import stock_generation_service
from .service.feedback_service import stock_feedback_service

router = APIRouter()


@router.post(
    "/ai/stock/generation",
    response_model=StockGenResponseDto,
    status_code=status.HTTP_201_CREATED
)
async def stock_generation_router(request: StockGenRequestDto) -> StockGenResponseDto:
    return await stock_generation_service(request)


@router.post(
    "/ai/stock/feedback",
    response_model=StockGenResponseDto,
    status_code=status.HTTP_201_CREATED
)
async def stock_feedback_router(request: FeedbackRequestDto) -> StockGenResponseDto:
    return await stock_feedback_service(request)
