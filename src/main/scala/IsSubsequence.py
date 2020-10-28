class Solution:
    def isSubsequence(self, s: str, t: str):
        n = len(s)
        m = len(t)
        l = 0
        r = 0
        while l < n and r < m:
            if s[l] == t[r]:
                l += 1
            r += 1
        return l == n