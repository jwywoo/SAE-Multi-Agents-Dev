from langgraph.graph import StateGraph, START, END
from ...schema.rag_schema import RAGFlowState
from ..nodes.retriever import retriever_node


def rag_flow_init():
    rag_graph = StateGraph(state_schema=RAGFlowState)

    # Registering Noes
    rag_graph.add_node("retriever_node", retriever_node)

    # Registering Edges
    rag_graph.add_edge(START, "retriever_node")
    rag_graph.add_edge("retriever_node", END)

    # Flow Init
    return rag_graph.compile()
