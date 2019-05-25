class Solution:
    def is_poly(self, s, i, j):
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True


    def longestPalindrome(self, s):
        if not s:
            return s
        max_len = 1
        start = 0
        poly = [0] * len(s)
        for i in range(len(poly)):
            poly[i] = [0] * len(s)
        for l in range(2, len(s) + 1):
             for i in range(len(s) - l + 1):
                j = i + l - 1
                if j == i:
                    continue
                if l == 2:
                    if s[i] == s[j]:
                        poly[i][j] = 2
                        if max_len < poly[i][j]:
                            start = i
                            max_len = poly[i][j]
                elif l % 2 == 0: # !!!!
                    if poly[i + 1][j - 1] > 0:
                        if s[i] == s[j]:
                            poly[i][j] = l
                            if max_len < poly[i][j]:
                                max_len = poly[i][j]
                                start = i
                else:
                    if self.is_poly(s, i, j):
                        poly[i][j] = l
                        if max_len < poly[i][j]:
                            max_len = poly[i][j]
                            start = i
        return s[start:start + max_len]

sol = Solution()

print(sol.longestPalindrome("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
print(sol.longestPalindrome("abccccdd"))
print(sol.longestPalindrome("a"))
print(sol.longestPalindrome("babad"))
print(sol.longestPalindrome("cbbd"))



