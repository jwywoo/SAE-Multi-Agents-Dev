from langchain.storage import InMemoryStore
from typing import Dict, Any
from .factory import default_preprocessed_result, default_rag_result


preprocessing_memory = InMemoryStore()
rag_memory = InMemoryStore()

memory_dict = {
    "preprocessing_memory": preprocessing_memory,
    "rag_memory": rag_memory
}

default_dict = {
    "preprocessing_memory": default_preprocessed_result,
    "rag_memory": default_rag_result
}


def add_memory(memory_name_space, key, value):
    selected_memory_store = memory_dict[memory_name_space]
    selected_memory_store.mset(
        [(key, value)]
    )


def get_memory(memory_name_space, key):
    selected_memory_store = memory_dict[memory_name_space]
    selected_value = selected_memory_store.mget([key])[0]
    if selected_value == None:
        return default_dict[memory_name_space](key)
    return selected_value
