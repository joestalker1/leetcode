class Solution:
    def countSegments(self, s):
        i = 0
        seg = 0
        while i < len(s):
            if (i == 0 or s[i-1] == ' ') and s[i] != ' ':
                seg += 1
            i += 1
        return seg

sol = Solution()
print(sol.countSegments("a a"))

