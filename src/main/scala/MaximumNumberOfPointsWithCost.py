class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        rows = len(points)
        cols = len(points[0])
        dp = [-1] * cols
        #firts row is just points[0]
        for i in range(cols):
            dp[i] = points[0][i]
        left_max = [-1] * cols
        right_max = [-1] * cols
        for i in range(1, rows):
            #new_dp = [-1] * cols
            #calc max poins[i][j] + j from the left to the right
            left_max[0] = dp[0]
            right_max[-1] = dp[cols-1] - cols + 1
            for j in range(1, cols):
                left_max[j] = max(left_max[j-1], dp[j] + j)
                k = cols - j - 1
                right_max[k] = max(right_max[k+1], dp[k] - k)
            #calc maximal points[j][j] - j from the right to the left
            for j in range(cols):
                dp[j] = max(left_max[j] - j,right_max[j] + j) + points[i][j]
        return max(dp)
