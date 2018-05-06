class Solution(object):
    def mySqrt(self, x):
        x0 = x
        s = float(x)
        d = 1
        while s > 1:
            s = s / 100
            if s > 1:
                d *= 10
                x0 = s
        if x0 >= 10:
            x0 = int(6 * d)
        else:
            x0 = int(2 * d)
        s = int(x)
        while abs(x0*x0 - s) >= 0.00001:
            x0 = 1/2*(x0 + s / x0)

        return int(x0)

sol = Solution()
print(sol.mySqrt(8))