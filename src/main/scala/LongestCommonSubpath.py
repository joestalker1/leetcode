class Solution:
    def longestCommonSubpath(self, n, paths):

        def RabinKarp(arr, L, q):
            al = (1 << (17 * L - 17)) % q
            t = 0
            d = 1 << 17
            all_hashes = set()
            # calculate hash of first L chars
            for i in range(L):
                t = (d * t + arr[i]) % q
            all_hashes.add(t)
            # add hashes of L-lenght substrings
            for i in range(1, len(arr) - L + 1):
                t = (d * (t - arr[i - 1] * al) + arr[i + L - 1]) % q
                all_hashes.add(t)
            return all_hashes

        MOD = (1 << 128) - 159
        lo = 0
        # calculate min of all pathes
        hi = min(len(p) for p in paths) + 1

        while lo + 1 < hi:
            # try length for common sequence
            L = (lo + hi) // 2
            # calculate hashes by length L for every paths and find common set in all sets of hashes.
            sets_of_hashes = [RabinKarp(p, L, MOD) for p in paths]
            common_set = set.intersection(*sets_of_hashes)
            if len(common_set) != 0:
                # if find lengths, let's increase probalitic. lenght of common sequence
                lo = L
            else:
                hi = L
        return lo