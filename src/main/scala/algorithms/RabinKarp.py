from collections import defaultdict

class RabinKarp:
    def search(L, a, n, nums, s):
        MOD = 10**9 + 7
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
