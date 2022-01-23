class Solution:
    def longestCommonSubpath(self, n, paths):

        def RabinKarp(arr, L):
            al = (1 << (17 * L - 17)) % MOD
            t = 0
            d = 1 << 17
            all_hashes = set()

            for i in range(L):
                t = (d * t + arr[i]) % MOD

            all_hashes.add(t)

            for i in range(1, len(arr) - L + 1):
                t = (d * (t - arr[i - 1] * al) + arr[i + L - 1]) % MOD
                all_hashes.add(t)

            return all_hashes

        m = len(paths)
        MOD = (1 << 128) - 159
        lo = 0
        hi = min(len(p) for p in paths) + 1

        while lo + 1 < hi:
            L = (lo + hi) // 2
            tt = set.intersection(*[RabinKarp(p, L) for p in paths])
            if len(tt) != 0:
                lo = L
            else:
                hi = L

        return lo