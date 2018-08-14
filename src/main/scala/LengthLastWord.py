class Solution:
    def lengthOfLastWord(self, s):
        s = s.strip()
        i = len(s) - 1
        while i >= 0 and s[i] != ' ':
            i -= 1
        lens = len(s) - i - 1
        if lens > 0:
            return lens
        return len(s)

sol = Solution()
print(sol.lengthOfLastWord("a b "))
print(sol.lengthOfLastWord("  "))
print(sol.lengthOfLastWord("a "))
print(sol.lengthOfLastWord("a a"))