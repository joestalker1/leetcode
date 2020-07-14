class Solution:
    def kSimilarity(self, A, B):
        if not A and not B:
            return 0
        if not A:
            return len(B)
        if not B:
            return len(A)
        n = len(A)
        dp = [[0] * (n+1)] * (n + 1)
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        perm = n - dp[-1][-1]
        return perm+1 if perm < n else perm


sol = Solution()
print(sol.kSimilarity(A = "abac", B = "baca"))
