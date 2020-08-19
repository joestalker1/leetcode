class Solution:
    def longestLine(self, M):
        if not M or len(M[0]) == 0:
            return 0
        n = len(M)
        m = len(M[0])
        # hor,vert, diag
        dph = [[0] * m for _ in range(n)]
        dpv = [[0] * m for _ in range(n)]
        dpd = [[0] * m for _ in range(n)]
        if M[0][0] == 1:
            dph[0][0] = 1
            dpv[0][0] = 1
            dpd[0][0] = 1
        if M[0][1] == 1:
            dph[0][1] = dph[0][0] + 1
        if M[1][0] == 1:
            dpv[1][0] = dpv[0][0] + 1
        if M[1][1] == 1:
            dpd[1][1] = dpd[0][0] +1

        max_len = 0
        for i in range(1, n):
            for j in range(1, m):
                if M[i][j] == 1:
                    dph[i][j] = max(dph[i][j], dph[i][j - 1] + 1)
                    dpv[i][j] = max(dpv[i][j], dpv[i - 1][j] + 1)
                    dpd[i][j] = max(dpd[i][j], dpd[i - 1][j - 1] + 1)
                    max_len = max(max_len, dpd[i][j],dph[i][j], dpv[i][j])
        return max_len


sol = Solution()
print(sol.longestLine([[0,1,1,0],[0,1,1,0],[0,0,0,1]]))
