class Solution:
    def detectCapitalUse(self, word):
        if not word:
            return False
        lower = 0
        for ch in word:
            if  'a' <= ch <= 'z':
                lower += 1
        if lower == len(word) or lower == 0 or lower == (len(word) - 1) and word[0].isupper():
            return True
        return False

sol = Solution()
print(sol.detectCapitalUse("aSa"))


