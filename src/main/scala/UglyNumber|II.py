class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)

        def lcm(a, b):
            return a * b // gcd(a, b)

        def count_ugly(x):
            # count numbers from [0:x] divisble by a
            sa = x // a
            # count numbers from [0:x] divisble by b
            sb = x // b
            # count numbers from [0:x] divisble by c
            sc = x // c
            # count numbers from [0:x] divible by a and b
            sab = x // lcm(a, b)
            # count numbers from [0:x] divible by b and c
            sbc = x // lcm(b, c)
            # count numbers from [0:x] divible by a and c
            sac = x // lcm(a, c)
            # count numbers from [0:x] divible by a,b and c
            sabc = x // lcm(a, lcm(b, c))
            # apply exculsive,inclusive rule
            return (sa + sb + sc - sab - sbc - sac + sabc)

        lo = 0
        hi = 10 ** 18
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if count_ugly(mid) < n:
                lo = mid + 1
            else:
                hi = mid
        return lo