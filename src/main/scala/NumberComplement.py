class Solution:
    def findComplement(self, num):
        comp = 0
        i = 0
        while num != 0 and i < 32:
            a = 1 - (num & 1)
            comp |= (a << i)
            num = num >> 1
            i += 1
        return comp

sol = Solution()
print(sol.findComplement(2))
print(sol.findComplement(1))
print(sol.findComplement(5))

