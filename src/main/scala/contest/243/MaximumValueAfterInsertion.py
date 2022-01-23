class Solution:
    def maxValue(self, n: str, x: int) -> str:
        # assert self._maxValue(123, 4) == 4123, 'increasing seq'
        # assert self._maxValue(123, 1) == 1231, 'increasing seq'
        # assert self._maxValue(321, 1) == 3211, 'decreasing seq'
        # assert self._maxValue(321, 2) == 3221, 'decreasing seq'
        # assert self._maxValue(-123, 3) == -1233, 'decreasing seq'
        return self._maxValue(n, x)

    def _maxValue(self, n: str, x: int):
        if not n:
            return 0
        if int(n) > 0:
            # find first digitst that is less
            for i in range(len(n)):
                if int(n[i]) <= x:
                    n = n[:i] + str(x) + n[i:]
                    break
            if i == len(n)-1:
                n += str(x)
        else:
            for i in range(1, len(n)):
                if int(n[i]) > x:
                    n = n[:i] + str(x) + n[i:]
                    break
            if i == len(n)-1:
                n += str(x)
        return n

s = Solution()
print(s.maxValue("-132", 3))