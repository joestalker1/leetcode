class Solution:
    def checkRecord(self, s):
        errors = False
        twoL = 0
        twoA = 0
        i = 0
        while i < len(s):
            if s[i] == 'A':
                twoA += 1
                if twoA > 1:
                    errors = True
                twoL = 0
            elif s[i] == 'L':
                twoL += 1
                if twoL > 2:
                    errors = True
                twoA = 0
            else:
                twoL = 0
                twoA = 0
            i += 1
        return not errors

sol = Solution()
print(sol.checkRecord("PPALLP"))
print(sol.checkRecord("PPALLL"))