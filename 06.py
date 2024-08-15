import string

def get_letter_range(user_input) :
    letters = string.ascii_letters
    start_letter, end_letter = user_input.split('-')
    start_index = letters.index(start_letter)
    end_index = letters.index(end_letter)
    return letters[start_index:end_index + 1]
user_input = input("введіть бкви наприклад 'а-с': ")
result = get_letter_range(user_input)
print(result)
