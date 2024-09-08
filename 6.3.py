user_number = int(input('Enter your integer number: '))

while user_number > 9:
    result = 1
    for i in str(user_number):
        result *= int(i)
    user_number = result

print(user_number)
