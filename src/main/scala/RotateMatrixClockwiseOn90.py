def rotate_matrix(matrix):
    n = len(matrix)

    for i in range(n // 2):
        for j in range(i, n - i - 1):
            p1 = matrix[i][j]
            p2 = matrix[j][n - i - 1]
            p3 = matrix[n - i - 1][n - j - 1]
            p4 = matrix[n - j - 1][i]
            #top-right assigns to top-left
            matrix[j][n - i - 1] = p1
            #bottom-right assigns to top-right
            matrix[n - i - 1][n - j - 1] = p2
            #bottom-left assigns to bottom-right
            matrix[n - j - 1][i] = p3
            #top-left assigns to bottom-left
            matrix[i][j] = p4
    return matrix


print(rotate_matrix([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]]))
