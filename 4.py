input_list = [1, 0, 13, 0, 0, 0, 5]
# lst = [0]
# lst = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
print("Origin list: ", input_list)

zero_qty = input_list.count(0)
while zero_qty > 0:
    input_list.remove(0)
    input_list.append(0)
    zero_qty -= 1
print("Modified list: ", input_list)
