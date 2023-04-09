class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        # assert self._minimizeSet(2,7,1,3) == 4,'test1'
        # assert self._minimizeSet(3, divisor2 = 5, uniqueCnt1 = 2, uniqueCnt2 = 1) == 3,'test2'
        # assert self._minimizeSet(2, divisor2 = 4, uniqueCnt1 = 8, uniqueCnt2 = 2) == 15, 'test3'
        # assert self._minimizeSet(12,3,2,10) == 14, 'test4'
        return self._minimizeSet(divisor1, divisor2, uniqueCnt1, uniqueCnt2)

    def _minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:

        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)

        def lcm(a, b):
            return a * b // gcd(a, b)

        lo = 1
        hi = 10 ** 10
        lcm_ab = lcm(divisor1, divisor2)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            num_not_div1 = mid - mid // divisor1
            num_not_div2 = mid - mid // divisor2
            # may be included in set1 and set 2
            num_not_div1_div2 = mid - mid // lcm_ab
            if num_not_div1 >= uniqueCnt1 and num_not_div2 >= uniqueCnt2 and num_not_div1_div2 >= uniqueCnt1 + uniqueCnt2:
                hi = mid
            else:
                lo = mid + 1
        return lo

