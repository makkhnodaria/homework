def correct_sentence(text: str) -> str:
    return (text[0].capitalize() + text[1:]).rstrip(".") + "."


result = correct_sentence("greetings, friends.")

print(result)