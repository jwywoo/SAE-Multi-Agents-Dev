import uuid

from .schema import StockGenRequestDto, ResponseDto, Stock, PreprocessingFlowState, RAGFlowState
from .preprocessing.flow.preprocessing_flow import preprocessing_flow_init
from .rag.flow.rag_flow import rag_flow_init

from .memory_store import add_memory, get_memory


async def stock_generation_service(request_dto: StockGenRequestDto) -> ResponseDto:
    preprocessing_flow_state = PreprocessingFlowState(
        state_id=str(uuid.uuid1()),
        request_dto=request_dto,
        route="",
        preprocessed_title="",
        preprocessed_url="",
        preprocessed_content="")
    # Preprocessing Flow
    # Preprocessing Agent Init
    preprocessing_agent = preprocessing_flow_init()
    preprocessed_result = preprocessing_agent.invoke(preprocessing_flow_state)
    add_memory(
        memory_name_space="preprocessing_memory",
        key=preprocessed_result['state_id'],
        value=preprocessed_result
    )

    # preprocessed_flow init for RAG
    rag_flow_state = RAGFlowState(
        state_id=preprocessed_result['state_id'],
        preprocessed_result={
            "title": preprocessed_result['preprocessed_title'],
            "url": preprocessed_result['preprocessed_url'],
            "content": preprocessed_result['preprocessed_content']
        },
        response_dto=[]
    )

    # RAG Flow
    # RAG Agent Init
    rag_agent = rag_flow_init()
    retrieved_result = rag_agent.invoke(rag_flow_state)
    add_memory(
        memory_name_space="rag_memory",
        key=retrieved_result['state_id'],
        value=retrieved_result
    )
    response_dto = ResponseDto(
        generated_stocks=[]
    )
    response_dto.generated_stocks.extend(retrieved_result['response_dto'])
    return response_dto
