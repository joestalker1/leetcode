class Solution:
    def nearestPalindromic(self, S):
        k = len(S)
        candidates = [str(10 ** l + d) for l in (k - 1, k) for d in (-1, 1)]
        p = int(S[:(k+1) // 2])
        for prefix in map(str, [p - 1, p, p + 1]):
            candidates.append(prefix + (prefix[:-1] if k % 2 != 0 else prefix)[::-1])

        def diff(x):
            return abs(int(x) - int(S))

        ans = None
        for cand in candidates:
            if cand != S and not cand.startswith('0'):
                if ans is None or diff(cand) < diff(ans) or diff(cand) == diff(ans) and cand == ans:
                    ans = cand
        return ans





sol = Solution()
print(sol.nearestPalindromic("23456"))
print(sol.nearestPalindromic("1000000"))
print(sol.nearestPalindromic("1234"))
print(sol.nearestPalindromic("123"))
