class Solution:
    def setZeroes(self, matrix):
        if not matrix:
            return
        rows = [0] * len(matrix)
        cols = [0] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows[i] = 1
                    cols[j] = 1

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if rows[i] == 1 or cols[j] == 1:
                    matrix[i][j] = 0


