from ..schema.base_schema import FeedbackRequestDto, StockGenResponseDto
from ..schema.feedback_schema import FeedbackFlowState

from ..memory_store import add_memory, get_memory

from ..feedback.flow.feedback_flow import feedback_flow_init


async def stock_feedback_service(request_dto: FeedbackRequestDto) -> StockGenResponseDto:
    state_id = request_dto.state_id
    preprocessing_flow_state = get_memory(
        memory_name_space="preprocessing_memory",
        key=state_id
    )

    rag_flow_state = get_memory(
        memory_name_space="rag_memory",
        key=state_id
    )
    feedback_flow_state = FeedbackFlowState(
        state_id=state_id,
        feedback_score=request_dto.feedback_score,
        regeneration=False,
        preprocessed_result=preprocessing_flow_state,
        rag_result=rag_flow_state
    )

    feedback_agent = feedback_flow_init()

    feedback_result = feedback_agent.invoke(feedback_flow_state)
    print("Regeneration Status: ", feedback_result['regeneration'])
    response_dto = StockGenResponseDto(
        state_id=state_id,
        generated_stocks=[]
    )
    return response_dto
