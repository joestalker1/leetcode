class Solution(object):
    def is_substr_poli(self, s, start, end):
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True

    def validPalindrome(self, s):
        if not s:
            return True
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return self.is_substr_poli(s, i + 1, j) or self.is_substr_poli(s, i, j - 1)
            i += 1
            j -= 1
        return True

sol = Solution()
print(sol.validPalindrome("abca"))
print(sol.validPalindrome("aba"))
