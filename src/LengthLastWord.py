class Solution:
    def lengthOfLastWord(self, s):
        for i in range(len(s) - 1, 0, -1):
            if s[i] == ' ':
                return len(s) - i - 1

        return 0

sol = Solution()
print(sol.lengthOfLastWord(False))