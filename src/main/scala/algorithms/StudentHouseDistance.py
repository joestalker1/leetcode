import math

class Solution:

    def matching(self, bit_mask, dist, memo, matching_value, n):
        if memo[bit_mask] > -0.5:
            return memo[bit_mask]
        if bit_mask == (1 << (2 * n)) - 1:#3ff
            memo[bit_mask] = 0
            return memo[bit_mask]
        #matching_value = 32767 ** 2

        for p1 in range(2 * n):# coordinate num is 2 * n
            if (bit_mask & (1 << p1)) == 0:# does i -student is matched...NO
                for p2 in range(p1 + 1, 2 * n):
                    if (bit_mask & (1 << p2)) == 0:# does j -student is matched...NO
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

    def run(self, x, y):
        matching_value = 32767 ** 2
        memo = [-1] * (1 << 16) #2 ^ 16
        n = int(len(x)) // 2 # numbers of groups.
        dist = [0] * (2 * n)
        for i in range(len(dist)):
            dist[i] = [0] * (2 * n)
        for i in range(len(dist)):
            for j in range(len(dist)):
                dist[i][j] = math.sqrt((x[i] - x[j]) * (x[i] - x[j]) + (y[i] - y[j]) * (y[i] - y[j]))
        #return min of sum (x1 + x2 + ... + xn)
        return self.matching(0, dist, memo, matching_value, n)

sol = Solution()
x = [10, 20, 5, 1, 120, 6, 50, 3, 6, 0]
y = [10, 10, 5, 1, 3, 6, 60, 24, 9, 0]
print(sol.run(x, y))





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