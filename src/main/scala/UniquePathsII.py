class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # assert self._uniquePathsWithObstacles([[0,0,0]]) == 1, '1 way'
        # assert self._uniquePathsWithObstacles([[0,1,0]]) == 0, '0 way'
        # assert self._uniquePathsWithObstacles([[0,0],[1,0]]) == 1, '1 way with 1 obstacle'
        # assert self._uniquePathsWithObstacles([[0,0],[0,0]]) == 2, '2 ways'
        return self._uniquePathsWithObstacles(obstacleGrid)

    def _uniquePathsWithObstacles(self, grid):
        if not grid or len(grid[0]) == 0 or grid[0][0] == 1 or grid[-1][-1] == 1:
            return 0
        n = len(grid)
        m = len(grid[0])
        dp = [0] * m
        dp[0] = 1
        for j in range(1, m):
            if grid[0][j] == 0:
                dp[j] += dp[j - 1]
        for i in range(1, n):
            new_dp = [0] * m
            for j in range(m):
                if grid[i][j] == 1:
                    continue
                if i > 0 and j > 0:
                    new_dp[j] = dp[j] + new_dp[j - 1]
                elif j > 0:
                    new_dp[j] += new_dp[j - 1]
                elif i > 0:
                    new_dp[j] += dp[j]
            dp = new_dp
        return dp[-1]