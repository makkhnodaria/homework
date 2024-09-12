def popular_words(text: str, words: list) -> dict:
    text_list = text.lower().split()
    res_dict = {}

    for elem in words:
        res_dict[elem] = text_list.count(elem)

    return res_dict


result = popular_words('''When I was One I had just begun When I was Two I was nearly new ''',
                       ['i', 'was', 'three', 'near'])

print(result)
