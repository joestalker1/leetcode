class NumMatrix(object):
    def __init__(self, matrix):
        self.aux = [0] * len(matrix)
        for i in range(len(matrix)):
            self.aux[i] = [0] * len(matrix[0])
        for j in range(len(matrix[0])):
            self.aux[0][j] = matrix[0][j]

        for i in range(1, len(self.aux)):
            for j in range(len(self.aux[i])):
                self.aux[i][j] = matrix[i][j] + self.aux[i-1][j]

        for i in range(len(self.aux)):
            for j in range(1, len(self.aux[i])):
                self.aux[i][j] += self.aux[i][j - 1]


    def sumRegion(self, row1, col1, row2, col2):
        if 0 == len(self.aux) or 0 == len(self.aux[0]):
            return 0
        sum_reg = self.aux[row2][col2]
        if row1 - 1 >= 0:
            sum_reg -= self.aux[row1-1][col2]
        if col1 - 1 >= 0:
            sum_reg -= self.aux[row2][col1 - 1]
        if row1 - 1 >= 0 and col1 - 1 >= 0:
            sum_reg += self.aux[row1-1][col1-1]
        return sum_reg


num_matrix = NumMatrix([[[]]])
print(num_matrix.sumRegion(0,0,0,0))
#print(num_matrix.sumRegion([[[]]]))
#print(num_matrix.sumRegion(2,1,4,3))



