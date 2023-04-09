class Solution:
    def appealSum(self, s: str) -> int:
        # assert self._appealSum('abbca') == 28,'test1'
        #assert self._appealSum('code') == 20, 'test2'
        #assert self._appealSum('abc') == 10, 'test3'
        return self._appealSum(s)

    def _appealSum(self, s: str) -> int:
        if not s:
            return 0
        def code(ch):
            return ord(ch) - ord('a')
        #count of substring ending by a char
        last = [0] * 26
        total = 0
        cur = 0
        for i in range(len(s)):
            #count substring ending at i and start from j + 1
            cur += i + 1 - last[code(s[i])]
            last[code(s[i])] = i + 1
            total += cur
        return total