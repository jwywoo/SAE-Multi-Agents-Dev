from langchain.storage import InMemoryStore


preprocessing_memory = InMemoryStore()
rag_memory = InMemoryStore()

memory_dict = {
    "preprocessing_memory": preprocessing_memory,
    "rag_memory": rag_memory
}


def add_memory(memory_name_space, key, value):
    selected_memory_store = memory_dict[memory_name_space]
    selected_memory_store.mset(
        [(key, value)]
    )


def get_memory(memory_name_space, key):
    selected_memory_store = memory_dict[memory_name_space]
    selected_value = selected_memory_store.mget([key])[0]
    return selected_value
