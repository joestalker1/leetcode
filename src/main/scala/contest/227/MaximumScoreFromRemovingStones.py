class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        a, b, c = sorted([a, b, c])
        # a + b <= c, then it results in a+b pairs
        if (a + b) <= c:
            return a + b
        # a + b > c, then decrease (a,c) and (b,c) until c = 0 and the  a== b,so it results in (a+b) / 2
        return c + (a + b - c) // 2
