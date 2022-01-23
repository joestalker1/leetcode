class Solution:
    def numWays(self, s: str) -> int:
        # assert self._numWays('111') == 1,'one way'
        # assert self._numWays('011') == 0, 'zero ways'
        # assert self._numWays('1011') == 2, 'zero ways'
        # assert self._numWays('000') == 1,  'one way'
        return self._numWays(s)

    def _numWays(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        zeros = 0
        for a in s:
            if a == '0':
                zeros += 1
        if len(s) == zeros:
            return ((len(s) - 1) * (len(s) - 2) // 2) % MOD
        ones = len(s) - zeros
        if ones % 3 != 0:
            return 0
        split_len = ones // 3
        cur_len = 0
        for i in range(len(s)):
            if s[i] == '1':
                cur_len += 1
            if cur_len == split_len:
                break
        i += 1
        split_second = [i, i]
        while i < len(s) and s[i] != '1':
            i += 1
        split_second[1] = i - 1
        cur_len = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '1':
                cur_len += 1
            if cur_len == split_len:
                break
        i -= 1
        split_third = [i, i]
        while i >= 0 and s[i] != '1':
            i -= 1
        split_third[0] = i + 1
        return (split_second[1] - split_second[0] + 2) * (split_third[1] - split_third[0] + 2) % MOD