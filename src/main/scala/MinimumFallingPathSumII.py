import heapq

class Solution:
    def minFallingPathSum(self, grid) -> int:
        # assert self._minFallingPathSum([[0,1],[0,1]]) == 1, 'test1'
        # assert self._minFallingPathSum([[0,1],[1,0]]) == 0, 'test2'
        return self._minFallingPathSum(grid)

    def _minFallingPathSum(self, grid) -> int:
        n = len(grid)
        for i in range(1, n):
            # find 2 minimum indexes
            min_val = heapq.nsmallest(2, grid[i - 1])
            for j in range(n):
                grid[i][j] += min_val[1] if grid[i - 1][j] == min_val[0] else min_val[0]
        return min(grid[-1])
