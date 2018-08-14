class Solution:
    def isPowerOfFour(self, num):
        while num >= 4:
            if num & 3 != 0:
                return False
            num = num >> 2
        return True if num == 1 else False

sol = Solution()
print(sol.isPowerOfFour(-64))

