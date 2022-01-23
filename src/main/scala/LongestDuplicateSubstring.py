from collections import defaultdict

class Solution:
    def longestDupSubstring(self, s: str) -> str:
        if len(s) < 1:
            return 0
        MOD = 10 ** 9 + 7

        def search(L, a, n, nums):
            h = 0
            for i in range(L):
                h = (h * a + nums[i]) % MOD

            seen = defaultdict(list)
            seen[h].append(0)
            al = pow(a, L, MOD)
            for start in range(1, n - L + 1):
                h = (h * (a - nums[start - 1] * al) + nums[start + L - 1]) % MOD
                if h in seen:
                    cur_s = s[start:start + L]
                    if any(cur_s == s[i:i + L] for i in seen[h]):
                        return start
                seen[h].append(start)
            return -1

        a = 26
        n = len(s)
        nums = [(ord(ch) - ord('a')) for ch in s]
        start = -1
        lo = 1
        hi = n - 1
        while lo <= hi:
            l = lo + (hi - lo) // 2
            pos = search(l, a, n, nums)
            if pos != -1:
                lo = l + 1
                start = pos
            else:
                hi = l - 1
        return s[start:start + lo - 1]
