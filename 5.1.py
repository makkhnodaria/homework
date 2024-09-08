import string
import keyword


result = True
name = input("Введіть рядок: ")
if len(name) > 1 and all(char == '_' for char in name):
    result = False
if name[0].isdigit():
    result = False
if any(char.isupper() or char in string.whitespace or char in string.punctuation.replace('_', '') for char in name):
    result = False
if name in keyword.kwlist:
    result = False

print(result)
