class Solution:
    def balancedStringSplit(self, s):
        if not s:
            return 0
        balanced = {'R':0,'L':0}
        i = 0
        res = 0
        while i < len(s):
            balanced[s[i]] += 1
            if balanced['R'] > 0 and balanced['L'] > 0 and (balanced['R'] + balanced['L']) % 2 == 0:
                #balanced['R'] = 0
                #balanced['L'] = 0
                res += 1
            i += 1
        return res

sol = Solution()
print(sol.balancedStringSplit("RRLRRLRLLLRL"))#2
#print(sol.balancedStringSplit("RRLRRLRLLLRL"))
#print(sol.balancedStringSplit("RLLLLRRRLR"))#4

