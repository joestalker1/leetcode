def bubble_swap(string, i, j):
    string = list(string)

    # Rotate so that i is at the beginning.
    while i > 0:
        string = string[1:] + string[:1]
        i -= 1

    # Move the first two letters to the end in reversed order.
    string = string[:1] + string[2:] + string[1:2]
    string = string[1:] + string[:1]

    # Rotate back to the initial position.
    while len(string) > j + 1:
        string = string[1:] + string[:1]
        j += 1

    return ''.join(string)


def get_best_word(string, k):
    string = list(string)

    if k == 1:
        best = string
        for i in range(1, len(string)):
            if string[i:] + string[:i] < best:
                best = string[i:] + string[:i]
        return ''.join(best)

    else:
        return ''.join(sorted(string))


print(get_best_word("zvdabc", 1))

