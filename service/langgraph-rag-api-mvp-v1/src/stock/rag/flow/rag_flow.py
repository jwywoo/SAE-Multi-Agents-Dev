from langgraph.graph import StateGraph, START, END
from ...schema import FlowState
from ..nodes.embedding import embedding_node
from ..nodes.retriever import retriever_node


def rag_flow_init():
    rag_graph = StateGraph(state_schema=FlowState)

    # Registering Noes
    rag_graph.add_node("embedding_node", embedding_node)
    rag_graph.add_node("retriever_node", retriever_node)

    # Registering Edges
    rag_graph.add_edge(START, "embedding_node")
    rag_graph.add_edge("embedding_node", "retriever_node")
    rag_graph.add_edge("retriever_node", END)

    # Flow Init
    return rag_graph.compile()
