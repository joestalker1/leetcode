MAX = 20002

class Solution:
    def minDominoRotations(self, A, B):
        if not A or not B:
            return -1
        for i in range(len(A)-1):
            if not (set([A[i], B[i]]) & set([A[i+1], B[i+1]])):
                return -1
        dp = [[MAX] * 2 for _ in range(len(A))]
        dp[0][0] = 0 # no swaps
        dp[0][1] = 1 # swap
        for i in range(1, len(A)):
            a = A[i]
            b = B[i]
            if a == A[i-1] or b == B[i-1]:
                dp[i][0] = min(dp[i-1][0], dp[i][0])
            if a == B[i-1] or b == A[i-1]:
                dp[i][0] = min(dp[i - 1][1], dp[i][0])

            #if swap A[i] and B[i]
            a = B[i]
            b = A[i]
            if a == A[i-1] or b == B[i-1]:
                dp[i][1] = min(dp[i-1][0] + 1, dp[i][1])
            if a == B[i-1] or b == A[i-1]:
                dp[i][1] = min(dp[i - 1][1]+1, dp[i][1])
        return min(dp[-1][0], dp[-1][1])


sol = Solution()
print(sol.minDominoRotations([2,1,1,3,2,1,2,2,1], [3,2,3,1,3,2,3,3,2]))
print(sol.minDominoRotations(A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]))






