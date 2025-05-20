from fastapi import APIRouter, status
from .schema import RequestDto, ResponseDto, FlowState, PreprocessingFlowState, RAGFlowState
from .service import stock_generation_service

router = APIRouter()


@router.post(
    "/ai/stock/generation",
    response_model=ResponseDto,
    status_code=status.HTTP_201_CREATED
)
async def stock_generation_router(request: RequestDto) -> ResponseDto:
    state = FlowState(
        request_dto=request,
        generated_stocks=[],
        preprocessing_flow_state=PreprocessingFlowState(
            route="",
            preprocessed_title="",
            preprocessed_url="",
            preprocessed_content=""
        ),
        rag_flow_state=RAGFlowState(
            route=""
        )
    )
    return await stock_generation_service(state)
