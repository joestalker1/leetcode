class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:

        def k_items_less(a):
            items = 0
            for r in range(1, m + 1):
                # count number that are multiple of r and <= a
                c = min(n, a // r)
                if c == 0:
                    break
                items += c
            return items >= k

        lo = 1
        hi = m * n
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if k_items_less(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
