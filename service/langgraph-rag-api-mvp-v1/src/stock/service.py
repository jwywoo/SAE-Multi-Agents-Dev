from .schema import FlowState, ResponseDto, Stock
from .preprocessing.flow.preprocessing_flow import preprocessing_flow_init
from .rag.flow.rag_flow import rag_flow_init


async def stock_generation_service(state: FlowState) -> ResponseDto:
    # Preprocessing Flow
    # Preprocessing Agent Init
    preprocessing_agent = preprocessing_flow_init()
    preprocessed_result = preprocessing_agent.invoke(state)

    # preprocessed_flow init for RAG
    preprocessed_flow = FlowState(
        request_dto=preprocessed_result['request_dto'],
        generated_stocks=preprocessed_result['generated_stocks'],
        preprocessing_flow_state=preprocessed_result['preprocessing_flow_state'],
        rag_flow_state=preprocessed_result['rag_flow_state'],
    )

    # RAG Flow
    # RAG Agent Init
    rag_agent = rag_flow_init()
    retrieved_result = rag_agent.invoke(preprocessed_flow)

    response_dto = ResponseDto(
        generated_stocks=[]
    )
    response_dto.generated_stocks.extend(retrieved_result['generated_stocks'])
    return response_dto
