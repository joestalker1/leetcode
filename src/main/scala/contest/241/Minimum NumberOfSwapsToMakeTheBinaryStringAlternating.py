class Solution:
    def minSwaps(self, s: str):
        # assert self._minSwaps('001') ==1, 'test0'
        # assert self._minSwaps('111') == -1, 'test1'
        # assert self._minSwaps('1010') == 0, 'test2'
        # assert self._minSwaps('1100') == 1, 'test3'
        return self._minSwaps(s)

    def _minSwaps(self, s: str) -> int:
        if not s:
            return 0
        zeros = 0
        s_len = len(s)
        for ch in s:
            if ch == '0':
                zeros += 1

        if s_len % 2 == 0 and zeros * 2 != s_len or abs(s_len - 2 * zeros) > 1:
            return -1

        def count_swaps(s, start):
            swaps = 0
            for ch in s:
                if ch != start:
                    swaps += 1
                start = str(ord('1') - ord(start))
            return swaps

        if s_len % 2 == 0:
            return min(count_swaps(s, '0'), count_swaps(s, '1')) // 2
        if zeros > s_len // 2:
            return count_swaps(s, '0') // 2
        return count_swaps(s, '1') // 2


sol = Solution()
print(sol.minSwaps("110000110"))#2
print(sol.minSwaps("110011010"))#2
