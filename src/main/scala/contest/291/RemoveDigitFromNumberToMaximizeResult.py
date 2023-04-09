class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        i = -1
        j = -1
        for k,ch in enumerate(number):
            if ch == digit and i == -1:
                j = i = k
            elif ch == digit:
                j = k
        a = list(number)
        a.pop(i)
        b = list(number)
        b.pop(j)
        return max(''.join(b), ''.join(a))


sol = Solution()
print(sol.removeDigit("133235", "3"))
print(sol.removeDigit( "1231","1"))#231