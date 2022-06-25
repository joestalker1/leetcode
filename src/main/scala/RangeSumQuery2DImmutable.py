class NumMatrix:
    def __init__(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        self.dp = [[0] * (m+1) for _ in range(n+1)]
        for i in range(n):
            for j in range(m):
                self.dp[i+1][j+1] = self.dp[i+1][j] + self.dp[i][j+1] + matrix[i][j] - self.dp[i][j]

    def sumRegion(self, row1, col1, row2, col2):
        return self.dp[row2+1][col2+1] - self.dp[row1][col2+1] - self.dp[row2+1][col1] + self.dp[row1][col1]


num_matrix = NumMatrix([[[]]])
print(num_matrix.sumRegion(0,0,0,0))
#print(num_matrix.sumRegion([[[]]]))
#print(num_matrix.sumRegion(2,1,4,3))



