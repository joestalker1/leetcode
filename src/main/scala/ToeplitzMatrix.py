def is_toeplitz(matrix):
    values = {}

    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if i - j not in values:
                values[i - j] = col
            elif values[i - j] != col:
                return False

    return True


print(is_toeplitz([[1, 2, 3, 4, 8],
                   [5, 1, 2, 3, 4],
                   [4, 5, 1, 2, 3],
                   [7, 4, 5, 1, 2]]))
