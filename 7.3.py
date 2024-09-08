def second_index(text: str, some_str: str) -> int or None:
    result = None

    index = text.find(some_str)
    if index != -1:
        index_second = text.find(some_str, index + 1)
        result = index_second if index_second != -1 else None

    return result


res_string = second_index("Hello, hello", "lo")

print(res_string)
