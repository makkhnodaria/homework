import random
lst = [random.randint(1, 100) for i in range(random.randint(3, 10))]
print("Origin list: ", lst)
new_lst = [lst[0], lst[2], lst[-2]]
print("Modified list: ", new_lst)
