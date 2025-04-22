from .schema import FlowState, ResponseDto, Stock
from .preprocessing.flow.preprocessing_flow import preprocessing_flow_init


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

    response = ResponseDto(
        generated_stocks=[]
    )
    response.generated_stocks.append(
        Stock(
            korean_name="test",
            english_name="test",
            market="test",
            ticker_code="test"
        )
    )
    return response
