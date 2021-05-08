import math

class Solution:
    def powmod(self, a, n, p):
        if n == 0:
            return 1
        if n % 2 == 0:
            return self.powmod((a*a) % p, n // 2, p)
        return (a * self.powmod((a*a) % p, (n-1) // 2, p)) % p

    def discreteLog(self, a, b, m):
        # a ^k = b % m, find k
        n = int(math.sqrt(m) + 1)
        # create map (a ^ k) % m => k for left part
        mm = {}
        for i in range(n, 0, -1):
            cur = self.powmod(a, i * n, m)
            mm[cur] = i
        # create right part
        for j in range(m):
            cur = (self.powmod(a, j, m) * b) % m
            if cur in mm:
                # p = i * n - j, i *n is in map.
                r = mm[cur] * n - j
                if r < m:
                    return r
        return -1


sol = Solution()
print(sol.discreteLog(2, 3, 5))



