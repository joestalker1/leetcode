class Solution:
    def minimumTotal(self, triangle):
        if not triangle:
            return 0
        dp = [tri for tri in triangle[-1]]
        for row in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[row])):
                dp[j] = min(dp[j], dp[j + 1]) + triangle[row][j]
        return dp[0]


sol = Solution()
print(sol.minimumTotal([[-1],[2,3],[1,-1,-3]]))

print(sol.minimumTotal([
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]))

