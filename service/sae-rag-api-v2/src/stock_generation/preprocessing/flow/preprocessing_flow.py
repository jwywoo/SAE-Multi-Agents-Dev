from langgraph.graph import StateGraph, START, END

from ..nodes.router_node import *
from ..nodes.preprocessing_nodes import *


def preprocessing_flow_init():
    preprocessing_graph = StateGraph(state_schema=PreprocessingFlowState)
    # Registering Noes

    # router
    preprocessing_graph.add_node(
        "preprocessing_router_node", preprocessing_router_node)

    # preprocessing
    preprocessing_graph.add_node(
        "naver_news_preprocessing_node", preprocessing_naver_news_node)
    preprocessing_graph.add_node(
        "naver_entertainment_preprocessing_node", preprocessing_naver_entertainment_node)
    preprocessing_graph.add_node(
        "naver_sports_preprocessing_node", preprocessing_naver_sports_node)
    preprocessing_graph.add_node(
        "youtube_preprocessing_node", preprocessing_youtube_node)

    # Registering Edges
    # Conditional Edges
    preprocessing_graph.add_edge(START, "preprocessing_router_node")

    preprocessing_graph.add_conditional_edges(
        "preprocessing_router_node",
        lambda flow_state: flow_state.route,
        {
            "naver_news": "naver_news_preprocessing_node",
            "naver_entertainment": "naver_entertainment_preprocessing_node",
            "naver_sports": "naver_sports_preprocessing_node",
            "youtube": "youtube_preprocessing_node",
            "default": END,
        }
    )

    preprocessing_graph.add_edge("naver_news_preprocessing_node", END)
    preprocessing_graph.add_edge("naver_entertainment_preprocessing_node", END)
    preprocessing_graph.add_edge("naver_sports_preprocessing_node", END)
    preprocessing_graph.add_edge("youtube_preprocessing_node", END)

    # agent Init
    return preprocessing_graph.compile()
