class Solution:
    def isPerfectSquare(self, num):
        if num <= 0:
            return False
        x0 = num
        while (x0 * x0) > num:
            x0 = 1/2*(x0 + num / x0)
            print(x0)
            # if x1 == x0:
            #     return False
            # else:
            #     x0 = x1
        return x0 % 1 == 0

sol = Solution()
print(sol.isPerfectSquare(5))