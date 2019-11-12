class Solution(object):
    def balancedStringSplit(self, s):
        if not s:
            return 0

        l = 0
        r = 0
        splits = 0
        for i in range(len(s)):
            if s[i] == 'L':
                l += 1
            elif s[i] == 'R':
                r += 1
            if l == r:
                l = 0
                r = 0
                splits += 1
        return splits

sol = Solution()
print(sol.balancedStringSplit("RRLRRLRLLLRL"))#2
print(sol.balancedStringSplit("LLLLRRRR"))#1
print(sol.balancedStringSplit("RLLLLRRRLR"))#3
print(sol.balancedStringSplit("RLRRLLRLRL"))#4







