def is_valid_input(txt:str):
    errors = []
    if len(txt) != 12:
        errors.append("Length must be 12 characters")
    if not txt[0].isalpha():
        errors.append("First character must be a letter")
    if not txt[1:].isdigit():
        errors.append("The rest of the characters must be digits")

    return (len(errors) == 0, errors)


print(is_valid_input("a14123456789"))