class Solution:
    def nthUglyNumber(self, n, a, b, c):
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)

        def lcm(a, b):
            return a * b // gcd(a, b)

        ab, bc, ac = lcm(a, b),lcm(b, c), lcm(a, c)
        abc = lcm(a, bc)
        lo = 1
        hi = 2 * 10 ** 9
        while lo < hi:
            mid = lo + (hi - lo) // 2
            cnt = mid // a + mid // b + mid // c - mid // ab - mid // ac - mid // bc + mid // abc
            if cnt < n:
                lo = mid + 1
            else:
                hi = mid
        return lo



sol = Solution()
print(sol.nthUglyNumber(n = 1000000000, a = 2, b = 217983653, c = 336916467))
#print(sol.nthUglyNumber(n = 5, a = 2, b = 11, c = 13))
print(sol.nthUglyNumber(3, 2, 3, 5))






