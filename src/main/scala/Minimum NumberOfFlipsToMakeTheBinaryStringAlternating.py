import math

class Solution:
    def minFlips(self, s: str) -> int:
        assert self._minFlips('000') == 1, 'one op'
        assert self._minFlips('111') == 1, 'one op'
        assert self._minFlips('101') == 0, 'one op'
        assert self._minFlips('010') == 0, 'one op'
        assert self._minFlips('1011') == 1, 'one op'
        return self._minFlips(s)

    def _minFlips(self, s: str) -> int:
        if not s:
            return 0
        lens = len(s)
        # concat s + s,to slide window and compare it with 101010.. and 010101... and choose minimal difference
        zero_mismatch = 0
        one_mismatch = 0
        arr = list(s)
        min_op = math.inf
        for i in range(2 * lens):
            if i < lens:
                arr[i] = ord(arr[i]) - ord('0')
            if i % 2 != arr[i % lens]:
                zero_mismatch += 1
            if (i + 1) % 2 != arr[i % lens]:
                one_mismatch += 1
            if i >= lens:
                if (i - lens) % 2 != arr[i - lens]:
                    zero_mismatch -= 1
                if (i - lens + 1) % 2 != arr[i - lens]:
                    one_mismatch -= 1
            if i >= lens - 1:
                min_op = min(min_op, zero_mismatch, one_mismatch)
        return min_op
