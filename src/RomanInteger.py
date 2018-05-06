class Solution(object):
    def posOf(self, order, x):
        for i in range(len(order)):
            if order[i] == x:
                return i


    def romanToInt(self, s):
        order = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        dec = [1, 5, 10, 50, 100, 500, 1000]
        num = 0
        i = 0
        while i < len(s):
            i1 = self.posOf(order, s[i])
            if i == len(s) - 1:
                num += dec[i1]
                i += 1
            else:
                i2 = self.posOf(order, s[i + 1])
                if i1 < i2:
                    num += dec[i2] - dec[i1]
                    i += 2
                else:
                    num += dec[i1]
                    i += 1
        return num

sol = Solution()
print(sol.romanToInt("MDCCCLXXXIV"))

print(sol.romanToInt("MCMXCVI"))

print(sol.romanToInt("MDCCLXXVI"))
