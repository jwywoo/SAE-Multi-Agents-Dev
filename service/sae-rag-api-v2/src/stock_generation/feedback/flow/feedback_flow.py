from langgraph.graph import StateGraph, START, END

from ...schema.feedback_schema import FeedbackFlowState
from ..nodes.feedback_nodes import *


def feedback_flow_init():
    feedback_graph = StateGraph(state_schema=FeedbackFlowState)

    feedback_graph.add_node("feedback_router_node", feedback_router_node)
    feedback_graph.add_node("regenerate_node", regenerate_node)
    feedback_graph.add_node("feedback_save_node", feedback_save_node)

    feedback_graph.add_edge(START, "feedback_router_node")
    feedback_graph.add_conditional_edges(
        "feedback_router_node",
        lambda flow_state: flow_state.regeneration,
        {
            True: "regenerate_node",
            False: "feedback_save_node",
        }
    )

    feedback_graph.add_edge("regenerate_node", END)
    feedback_graph.add_edge("feedback_save_node", END)

    return feedback_graph.compile()
