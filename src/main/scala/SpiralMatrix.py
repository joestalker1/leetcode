def add_new_round(matrix, buf, r1, c1, r2, c2):
    # add top row
    for i in range(c1, c2 + 1):
        buf.append(matrix[r1][i])
    # add right side
    for i in range(r1 + 1, r2 + 1):
        buf.append(matrix[i][c2])
    # add bottom row
    if r2 > r1:
        for i in range(c2 - 1, c1 - 1, -1):
            buf.append(matrix[r2][i])
    # add left side
    if c2 > c1:
        for i in range(r2 - 1, r1, -1):
            buf.append(matrix[i][c1])


def spiral_copy(inputMatrix):
    if not inputMatrix:
        return []
    r1 = 0
    c1 = 0
    r2 = len(inputMatrix) - 1
    c2 = len(inputMatrix[0]) - 1
    res = []
    while r1 <= r2 and c1 <= c2:
        add_new_round(inputMatrix, res, r1, c1, r2, c2)
        r1 += 1
        c2 += 1
        r2 -= 1
        c2 -= 1
    return res

print(spiral_copy([[1],[2]]))