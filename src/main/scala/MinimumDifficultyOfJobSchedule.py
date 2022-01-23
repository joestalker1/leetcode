import math

class Solution:
    def minDifficulty(self, jobDifficulty, d: int) -> int:
        # assert self._minDifficulty([1,1],2) == 2, 'greater days'
        # assert self._minDifficulty([1,2],2) == 3, 'greater jobs'
        # assert self._minDifficulty([1,2,3], 2) == 4, 'increasing difficulties'
        # assert self._minDifficulty([3,2,1], 2) == 4, 'decreasing difficulties'
        # assert self._minDifficulty([1,2,3, 1], 2) == 4, 'slope jobs'
        # assert self._minDifficulty([1,2,3, 1], 3) == 5, 'slope jobs'
        return self._minDifficulty(jobDifficulty, d)

    def _minDifficulty(self, jobDifficulty, d: int) -> int:
        if not jobDifficulty or d > len(jobDifficulty):
            return -1
        dp = [[math.inf] * d for _ in range(len(jobDifficulty))]
        dp[0][0] = jobDifficulty[0]
        for i in range(1, len(jobDifficulty)):
            dp[i][0] = max(dp[i - 1][0], jobDifficulty[i])

        for i in range(1, len(jobDifficulty)):
            # it doesn't make sense to consider if [0:i] < d
            for j in range(1, min(i + 1, d)):
                local_max = 0
                for k in range(i - 1, -1, -1):
                    # take if it has solution for [0:k][d-1]
                    local_max = max(local_max, jobDifficulty[k + 1])
                    dp[i][j] = min(dp[i][j], dp[k][j - 1] + local_max)
        return dp[-1][-1]

sol = Solution()
print(sol.minDifficulty([6,5,4,3,2,1], 2))
