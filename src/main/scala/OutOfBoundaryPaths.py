from functools import lru_cache

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        if m == 0 or n == 0:
            return 0
        # m is row number, n is column number
        MOD = 10 ** 9 + 7

        @lru_cache(None)
        def find_path(r, c, left_moves):
            if r == m or r < 0 or c == n or c < 0:
                return 1
            if left_moves == 0:
                return 0
            return find_path(r + 1, c, left_moves - 1) + find_path(r - 1, c, left_moves - 1) + find_path(r, c - 1,
                                                                                                         left_moves - 1) + find_path(
                r, c + 1, left_moves - 1)

        return find_path(startRow, startColumn, maxMove) % MOD