class Solution:
    def minFallingPathSum(self, matrix) -> int:
        # assert self._minFallingPathSum([[0,1],[0,1]]) == 0, 'test1'
        # assert self._minFallingPathSum([[1,1],[0,1]]) == 1, 'test2'
        # assert self._minFallingPathSum([[0,1],[1,0]]) == 0, 'test3'
        return self._minFallingPathSum(matrix)

    def _minFallingPathSum(self, matrix) -> int:
        n = len(matrix)
        for i in range(1, n):
            for j in range(n):
                matrix[i][j] += min(matrix[i - 1][j], matrix[i - 1][j - 1] if j > 0 else inf,
                                    matrix[i - 1][j + 1] if j + 1 < n else inf)
        return min(matrix[-1])
