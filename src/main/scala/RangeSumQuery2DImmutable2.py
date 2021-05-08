class NumMatrix:

    def __init__(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        self.sum_matrix = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                self.sum_matrix[i][j] = matrix[i][j]
                if i > 0 and j > 0:
                    self.sum_matrix[i][j] += self.sum_matrix[i][j-1]+self.sum_matrix[i-1][j] - self.sum_matrix[i-1][j-1]
                elif i > 0:
                    self.sum_matrix[i][j] += self.sum_matrix[i-1][j]
                elif j > 0:
                    self.sum_matrix[i][j] += self.sum_matrix[i][j-1]

    def sumRegion(self, row1, col1, row2, col2):
        res = self.sum_matrix[row2][col2]
        if row1 > 0 and col1 > 0:
            res += self.sum_matrix[row1 - 1][col1 - 1]
        if row1 > 0:
            res -= self.sum_matrix[row1 - 1][col2]
        if col1 > 0:
            res -= self.sum_matrix[row2][col1 - 1]
        return res
