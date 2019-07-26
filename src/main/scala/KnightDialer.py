class Solution(object):
    def knightDialer(self,  N):
        if N <= 0:
            return 0
        m = {}
        m[0] = [4, 6]
        m[1] = [6, 8]
        m[2] = [7, 9]
        m[3] = [4, 8]
        m[4] = [0, 3, 9]
        m[5] = []
        m[6] = [1, 7, 0]
        m[7] = [2, 6]
        m[8] = [1, 3]
        m[9] = [4, 2]
        dp = [0] * (N + 1)
        for i in range(len(dp)):
            dp[i] = [0] * 10
        for i in range(10):
            dp[1][i] = 1

        for i in range(2, N + 1):
            for j in range(0, 10):
                for c in m[j]:
                    dp[i][j] += dp[i-1][c]
        return sum(dp[N]) % (10 ** 9 + 7)


sol = Solution()
print(sol.knightDialer(100))
#print(sol.knightDialer(4))
print(sol.knightDialer(1))#10
print(sol.knightDialer(2))#20
print(sol.knightDialer(3))#46



