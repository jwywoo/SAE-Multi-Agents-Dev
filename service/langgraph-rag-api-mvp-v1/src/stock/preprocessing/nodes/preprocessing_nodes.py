from .supporting_tools import content_parser

from ...schema import FlowState


def preprocessing_naver_news_node(state: FlowState):
    preprocessing_flow_state = state.preprocessing_flow_state
    requestDto = state.request_dto
    """Cleans Naver News content."""
    preprocessing_flow_state.preprocessed_content = content_parser(
        requestDto.original_content, remove_after="copyright .*?\. all rights reserved")
    preprocessing_flow_state.preprocessed_content = content_parser(
        requestDto.original_content, remove_after="기사 공유하기")
    preprocessing_flow_state.preprocessed_content = content_parser(requestDto.original_content, patterns=[
        r"본문 바로가기", r"naver", r"뉴스", r"엔터", r"스포츠", r"날씨", r"프리미엄",
        r"사용자 링크", r"로그인", r"서비스", r"더보기", r"검색", r"언론사별", r"정치",
        r"경제", r"사회", r"생활문화", r"it과학", r"세계", r"랭킹", r"신문보기",
        r"오피니언", r"tv", r"팩트체크", r"알고리즘 안내", r"정정보도 모음"])
    return state


def preprocessing_naver_entertainment_node(state: FlowState):
    preprocessing_flow_state = state.preprocessing_flow_state
    requestDto = state.request_dto

    """Cleans Naver Entertainment content."""
    preprocessing_flow_state.preprocessed_content = content_parser(
        requestDto.original_content, remove_after="copyright .*?\. all rights reserved")
    preprocessing_flow_state.preprocessed_content = content_parser(
        requestDto.original_content, remove_after="기사 공유하기")
    preprocessing_flow_state.preprocessed_content = content_parser(requestDto.original_content, patterns=[
        r"본문 바로가기", r"naver", r"엔터", r"뉴스", r"스포츠", r"사용자 링크", r"로그인",
        r"검색", r"홈", r"드라마", r"영화", r"뮤직", r"연애", r"포토", r"랭킹", r"최신뉴스", r"연재", r"종합"])
    return state


def preprocessing_naver_sports_node(state: FlowState):
    preprocessing_flow_state = state.preprocessing_flow_state
    requestDto = state.request_dto
    """Cleans Naver Sports content."""
    preprocessing_flow_state.preprocessed_content = content_parser(
        requestDto.original_content, remove_after="copyright .*?\. all rights reserved")
    preprocessing_flow_state.preprocessed_content = content_parser(
        requestDto.original_content, remove_after="기사 공유하기")
    return state


def preprocessing_youtube_node(state: FlowState):
    preprocessing_flow_state = state.preprocessing_flow_state
    requestDto = state.request_dto
    """Cleans YouTube transcript content."""
    preprocessing_flow_state.preprocessed_content = content_parser(
        requestDto.original_content, remove_after="더보기")
    preprocessing_flow_state.preprocessed_content = content_parser(
        requestDto.original_content, patterns=[r"kr", r"탐색", r"건너뛰기", r"만들기"])
    return state
