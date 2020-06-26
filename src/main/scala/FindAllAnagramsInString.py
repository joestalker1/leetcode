from collections import Counter
from collections import defaultdict


class Solution:
    def findAnagrams(self, s, p):
        if not s or not p or len(s) < len(p):
            return []
        pat = Counter(p)
        win = defaultdict(int)
        res = []
        for i in range(len(s)):
            win[s[i]] += 1
            # remove leftside chars
            if i >= len(p):
                if win[s[i - len(p)]] == 1:
                    del win[s[i - len(p)]]
                else:
                    win[s[i - len(p)]] -= 1
            if win == pat:
                res.append(i - len(p) + 1)
        return res


sol = Solution()
print(sol.findAnagrams("abaacbabc", "abc"))  # [3,4,6]
# print(sol.findAnagrams("abacbabc", "abc"))
print(sol.findAnagrams("abab", "ab"))
print(sol.findAnagrams("cbaebabacd", "abc"))
