def find_unique_value(some_list: list):
    result = None
    for elem in some_list:
        if some_list.count(elem) == 1:
            result = elem
            break

    return result


print(find_unique_value([5, 5, 5, 2, 2, 0.5]))
