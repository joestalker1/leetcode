class Solution:
    def maximalSquare(self, matrix):
        if not matrix:
            return 0
        dp = [0] * (len(matrix) + 1)
        for i in range(len(dp)):
            dp[i] = [0] * (len(matrix[0]) + 1)
        max_len = 0
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if matrix[i - 1][j - 1] == '1':
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    max_len = max(max_len, dp[i][j])
        return max_len * max_len




sol = Solution()
arr = [["0","0","0","0","1","1","1","0","1"],["0","0","1","1","1","1","1","0","1"],["0","0","0","1","1","1","1","1","0"]]
print(sol.maximalSquare(arr))

arr = [["1","0","1","0"],["1","0","1","1"],["1","0","1","1"],["1","1","1","1"]]
#print(sol.maximalSquare(arr))
arr = [["1","1"],["1","1"]]
#print(sol.maximalSquare(arr))
arr = [[1, 0, 1, 0, 0],
       [1, 0, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 0, 0, 1, 0]]
#print(sol.maximalSquare(arr))







        
