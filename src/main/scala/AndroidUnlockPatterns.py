class Solution:
    def numberOfPatterns(self, m, n):

        def dfs(seen, skip, cur, rem):
            if rem == 0:
                return 1
            if rem < 0:
                return 0
            seen.add(cur)
            ret = 0
            for i in range(1,10):
                if i not in seen and (skip[i][cur] == 0 or skip[i][cur] in seen):
                    ret += dfs(seen, skip, i, rem - 1)
            seen.discard(cur)
            return ret

        res = 0
        skip = [[0] * 10 for _ in range(10)]
        # encode intermidiate number
        skip[1][3] = skip[3][1] = 2
        skip[1][7] = skip[7][1] = 4
        skip[7][9] = skip[9][7] = 8
        skip[3][9] = skip[9][3] = 6
        skip[1][9] = skip[9][1] = skip[2][8] = skip[8][2] = skip[3][7] = skip[7][3] = skip[4][6] = skip[6][4] = 5
        seen = set()
        for i in range(m, n+1):
            res += (dfs(seen, skip, 1, i - 1) * 4)
            res += (dfs(seen, skip, 2, i - 1) * 4)
            res += dfs(seen, skip, 5, i - 1)
        return res



sol = Solution()
print(sol.numberOfPatterns(1, 3))