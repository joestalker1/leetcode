# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

def guess(num):
    pass

class Solution:
    def guessNumber(self, n: int) -> int:
        lo = 1
        hi = n
        while lo <= hi:
            mid = lo + (hi - lo)//2
            g = guess(mid)
            if g == 0:
                return mid
            if g == -1:
                hi = mid -1
            else:
                lo = mid + 1

