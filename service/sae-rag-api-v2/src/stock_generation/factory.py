from typing import Dict, Any
from .schema.base_schema import StockGenRequestDto


def default_preprocessed_result(key: str) -> Dict[str, Any]:
    return {
        "state_id": key,
        "request_dto": StockGenRequestDto(
            original_title="string",
            original_url="string",
            original_content="string"
        ),
        "route": "default",
        "preprocessed_title": "string",
        "preprocessed_url": "string",
        "preprocessed_content": "string"
    }


def default_rag_result(key: str) -> Dict[str, Any]:
    return {
        "state_id": key,
        "preprocessed_result": {
            "title": "string",
            "url": "string",
            "content": "string"
        },
        "response_dto": []
    }
