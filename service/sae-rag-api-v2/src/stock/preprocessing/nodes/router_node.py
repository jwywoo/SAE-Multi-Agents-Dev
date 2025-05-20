import re

from .supporting_tools import text_cleaning

from ...schema import FlowState


def preprocessing_router_node(state: FlowState):
    request_dto = state.request_dto
    preprocessing_flow_state = state.preprocessing_flow_state

    youtube_pattern = r"^https?://(www\.)?youtube\.com"
    naver_news_pattern = r"^https?://n\.news\.naver\.com"
    naver_entertainment_pattern = r"^https?://m\.entertain\.naver\.com"
    naver_sports_pattern = r"^https?://m\.sports\.naver\.com"

    if re.match(naver_news_pattern, request_dto.original_url):
        route = "naver_news"

    elif re.match(naver_entertainment_pattern, request_dto.original_url):
        route = "naver_entertainment"

    elif re.match(naver_sports_pattern, request_dto.original_url):
        route = "naver_sports"

    elif re.match(youtube_pattern, request_dto.original_url):
        route = "youtube"
    else:
        route = "default"

    # Basic text cleaning
    preprocessing_flow_state.preprocessed_title = text_cleaning(
        request_dto.original_title)
    preprocessing_flow_state.preprocessed_content = text_cleaning(
        request_dto.original_content)
    preprocessing_flow_state.preprocessed_url = request_dto.original_url
    preprocessing_flow_state.route = route

    state.preprocessing_flow_state = preprocessing_flow_state
    return state
