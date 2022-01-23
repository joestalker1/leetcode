class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) == 0 or len(bloomDay) < m * k:
            return -1

        def make_bukey(days):
            bouquets = 0
            flowers = 0
            for d in bloomDay:
                if d > days:
                    flowers = 0
                else:
                    flowers += 1
                    bouquets += flowers // k
                    flowers %= k
            return bouquets >= m

        lo = min(bloomDay)
        max_day = max(bloomDay)
        hi = max_day
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if make_bukey(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
