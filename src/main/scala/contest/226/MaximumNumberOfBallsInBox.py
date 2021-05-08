from collections import defaultdict

class Solution:
    def countBalls(self, lowLimit, highLimit):
        m = defaultdict(int)
        for b in range(lowLimit, highLimit + 1):
            a = b
            s = 0
            while a:
                s += (a % 10)
                a = a // 10
            m[s] += 1
        return max(m.values())




