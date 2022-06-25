class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return s

        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1

        start = 0
        end = 0
        for i in range(len(s)):
            poly_len1 = expand(i, i)
            poly_len2 = expand(i, i + 1)
            max_len = max(poly_len1, poly_len2)
            if max_len > end - start:
                start = i - max_len // 2
                end = i + max_len // 2
                if max_len % 2 == 0:
                    start += 1
        return s[start:end + 1]