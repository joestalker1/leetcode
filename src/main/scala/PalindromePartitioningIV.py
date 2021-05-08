class Solution:
    def checkPartitioning(self, s):
        n = len(s)
        pol = [[False] * n for _ in range(n)]
        for i in range(n):
            pol[i][i] = True
        for l in range(2, n):
            for i in range(n):
                j = i + l - 1
                if j == n:
                    break
                if s[i] == s[j] and (l == 2 or pol[i+1][j-1]):
                    pol[i][j] = True

        for i in range(n - 2):
            if not pol[0][i]:
                continue
            j = n - 1
            while j > i:
                if pol[j][n-1] and pol[i+1][j-1]:
                    return True
                j -= 1
        return False


sol = Solution()
print(sol.checkPartitioning("bcbddxy"))
print(sol.checkPartitioning("abcbdd"))

