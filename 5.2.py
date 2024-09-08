while True:
    first_number = int(input("input the first number: "))
    second_number = int(input("input the second number: "))
    action = input("input the sign for calculation action: ")

    if action == "+":
        print("a + b =", first_number + second_number)
    elif action == "-":
        print("a - b =", first_number - second_number)
    elif action == "*":
        print("a * b =", first_number * second_number)
    elif action == "/":
        if second_number == 0:
            print("The denominator can't be 0. Calculation can't be done")
        else:
            print("a / b =", first_number / second_number)
    else:
        print("Please choose one of the following simbols for calculation: +, -, *, /")

    answer = input("Do you want continue? (yes/y)").lower()
    if answer not in ('yes', 'y'):
        break
