from ...schema import RAGFlowState, Stock

from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone
from typing import List
from langchain_openai import OpenAIEmbeddings
from typing_extensions import Annotated

from config import get_settings
settings = get_settings()


def retriever_init(index_name: str, embeddings, namespace):
    pc = Pinecone(api_key=settings.PINECONE_API_KEY)
    index = pc.Index(index_name)
    vector_store = PineconeVectorStore(index=index, embedding=embeddings)
    return vector_store.as_retriever(
        search_type="similarity_score_threshold",
        search_kwargs={"k": 2, "score_threshold": 0.65, "namespace": namespace},)


def retrieved_vector_parser(given_vectors, market_name="N/A"):
    return [
        Stock(
            korean_name=vector.metadata.get("korean_name", "N/A"),
            english_name=vector.metadata.get("english_name", "N/A"),
            ticker_code=vector.metadata.get("ticker_code", "N/A"),
            market=market_name
        )
        for vector in given_vectors
    ]


def retriever_node(rag_flow_state: RAGFlowState):
    text = f"{rag_flow_state.preprocessed_result['title']}  {rag_flow_state.preprocessed_result['content']}"

    # Vector Store init
    embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
    kor_retriever = retriever_init(
        "sae-embedded-stocks-kor", embeddings, "kospi-900")
    foriegn_retriever = retriever_init(
        "sae-embedded-stocks-foriegn", embeddings, "nasdaq-1000")

    # Invoke
    kor_result = retrieved_vector_parser(kor_retriever.invoke(text), "KOSPI")
    foriegn_result = retrieved_vector_parser(
        foriegn_retriever.invoke(text), "NASDAQ")
    rag_flow_state.response_dto.extend(kor_result)
    rag_flow_state.response_dto.extend(foriegn_result)
    return rag_flow_state
