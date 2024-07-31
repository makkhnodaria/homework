my_list = [24, 75, 22, 83, 90]
def move_last_to_first(lst):
    if len(lst) == 0 or len(lst) == 1:
        return lst
    last_element = lst.pop()
    lst.insert(0, last_element)
    return lst

my_list = [24, 75, 22, 83, 90]
new_list = move_last_to_first(my_list)
print(new_list)
