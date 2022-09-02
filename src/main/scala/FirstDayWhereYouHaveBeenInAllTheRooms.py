class Solution:
    def firstDayBeenInAllRooms(self, nextVisit) -> int:
        if not nextVisit:
            return 0
        MOD = 10 ** 9 + 7
        n = len(nextVisit)
        f = [0] * n
        g = [0] * n
        f[0] = 1
        g[0] = 2
        for i in range(1, n):
            f[i] = (g[i-1] + 1) % MOD
            g[i] = (2*f[i] - f[nextVisit[i]] + 1 + MOD) % MOD
        return (f[n-1] - 1 + MOD) % MOD
    