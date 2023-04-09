class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        # assert self._minimizedMaximum(6,[11,6]) == 3, 'test1'
        # assert self._minimizedMaximum(7,[15,10,10]) == 5, 'test2'
        # assert self._minimizedMaximum(1,[1000]) == 1000, 'test3'
        return self._minimizedMaximum(n, quantities)

    def _minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        if len(quantities) == n:
            return max(quantities)

        lo = 1
        hi = max(quantities)
        amount = 0
        while lo < hi:
            amount = lo + (hi - lo) // 2
            cur_shop = sum([(q + amount - 1) // amount for q in quantities])
            if cur_shop > n:
                lo = amount + 1
            else:
                hi = amount
        return lo

