class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        #x = p*q, we need p + q strokes to get x chars
        d = 2
        cnt = 0
        while n > 1:
            while n % d == 0:
                cnt += d
                n = n // d
            d += 1
        return cnt
    