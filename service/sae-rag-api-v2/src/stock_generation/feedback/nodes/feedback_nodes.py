from ...schema.feedback_schema import FeedbackFlowState


def feedback_router_node(feedback_flow_state: FeedbackFlowState):
    if (feedback_flow_state.feedback_score <= 3):
        feedback_flow_state.regeneration = True
    return feedback_flow_state


def regenerate_node(feedback_flow_state: FeedbackFlowState):
    return feedback_flow_state


def feedback_save_node(feedback_flow_state: FeedbackFlowState):
    return feedback_flow_state
