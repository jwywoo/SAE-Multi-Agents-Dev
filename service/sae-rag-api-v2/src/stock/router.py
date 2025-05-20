from fastapi import APIRouter, status
from .schema import StockGenRequestDto, ResponseDto
from .service import stock_generation_service

router = APIRouter()


@router.post(
    "/ai/stock/generation",
    response_model=ResponseDto,
    status_code=status.HTTP_201_CREATED
)
async def stock_generation_router(request: StockGenRequestDto) -> ResponseDto:
    return await stock_generation_service(request)
