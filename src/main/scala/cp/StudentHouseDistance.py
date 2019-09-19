import math

class Solution:

    def matching(self, bit_mask, dist, memo, matching_value, n):
        # dist = [0] * 20
        # for i,row in enumerate(dist):
        #     row[i] = [0] * 20
        # memo = [0] * (1 << 16) #2 ^ 16

        if memo[bit_mask] > -0.5:
            return memo[bit_mask]
        if bit_mask == (1 << (2 * n)) - 1:#3ff
            memo[bit_mask] = 0
            return memo[bit_mask]
        #matching_value = 32767 ** 2

        for p1 in range(2 * n):
            if (bit_mask & (1 << p1)) == 0:
                for p2 in range(p1 + 1, 2 * n):
                    if (bit_mask & (1 << p2)) == 0:
                        matching_value = min(matching_value,
                                         dist[p1][p2] + self.matching(bit_mask | (1 << p1) | (1 << p2), dist, memo, matching_value, n))
                break
        memo[bit_mask] = matching_value
        return memo[bit_mask]

    def run(self):
        matching_value = 32767 ** 2
        memo = [-1] * (1 << 16) #2 ^ 16
        n = int(raw_input())
        x = [0] * (2 * n)
        y = [0] * (2 * n)
        for i in range(2 * n):
            s = raw_input()
            name,xx,yy = s.split()
            x[i] = int(xx)
            y[i] = int(yy)
        dist = [0] * (2*n)
        for i in range(len(dist)):
            dist[i] = [0] * (2*n)
        for i in range(len(dist)):
            for j in range(len(dist)):
                dist[i][j] = math.sqrt((x[i] - x[j]) * (x[i] - x[j]) + (y[i] - y[j]) * (y[i] - y[j]))
        return self.matching(0, dist, memo, matching_value, n)

sol = Solution()
print(sol.run())





# 5
# sohel 10 10
# mahmud 20 10
# sanny 5 5
# prince 1 1
# per 120 3
# mf 6 6
# kugel 50 60
# joey 3 24
# limon 6 9
# manzoor 0 0