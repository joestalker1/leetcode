import math

class Solution:
    def palindromicPartition(self, string):
        # code here
        n = len(string)
        cut = [0] * n
        p = [[0] * n for _ in range(n)]
        for i in range(n):
            p[i][i] = True
        for l in range(2, n+1):
            for i in range(n-l+1):
                j = i + l - 1
                if l == 2:
                    p[i][j] = string[i] == string[j]
                else:
                    p[i][j] = (string[i] == string[j]) and p[i+1][j-1]
        for i in range(n):
            if p[0][i]:
                cut[i] = 0
            else:
                cut[i] = math.inf
                for j in range(i):
                    if p[j+1][i] and 1 + cut[j] < cut[i]:
                        cut[i] = cut[j] + 1
        return cut[n-1]

sol = Solution()
print(sol.palindromicPartition('ababbbabbababa'))