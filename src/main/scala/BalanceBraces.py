def get_closest_string(s):
    closest_string = []

    open_parens = 0

    for char in s:
        if char == "(":
            open_parens += 1
            closest_string.append(char)

        else:
            if not open_parens:
                closest_string.append("(")
            else:
                open_parens -= 1
            closest_string.append(char)
    # check if last chare are closest braces.
    while open_parens:
        open_parens -= 1
        closest_string.append(")")

    return ''.join(closest_string)


print(get_closest_string("))()("))