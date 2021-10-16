class Solution:
    def maxMatrixSum(self, matrix) -> int:
        neg_cnt = 0
        max_sum = 0
        min_num = abs(matrix[0][0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                max_sum += abs(matrix[i][j])
                min_num = min(min_num, abs(matrix[i][j]))
                if matrix[i][j] < 0:
                    neg_cnt += 1
        if neg_cnt % 2 == 0:
            return max_sum
        return max_sum - 2 * min_num

