def pascal(k):
    rows = [[0 for _ in range(k)] for _ in range(k)]

    rows[0][0] = 1
    for i in range(1, k):
        for j in range(i + 1):
            rows[i][j] = rows[i - 1][j - 1] + rows[i - 1][j]

    return rows[-1]


print(pascal(4))