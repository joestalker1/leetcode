class Solution:
    def smallestDistancePair(self, nums, k: int) -> int:
        # assert self._smallestDistancePair([],2) == 0, 'empty array'
        # assert self._smallestDistancePair([1,1,2],2) == 1,'2 pairs'
        # assert self._smallestDistancePair([1,3,4],2) == 2, '1 pair'
        return self._smallestDistancePair(nums, k)

    def _smallestDistancePair(self, nums, k: int):
        if not nums or len(nums) * (len(nums) - 1) // 2 < k:
            return 0

        def feasible(dist):
            l = 0
            r = 0
            # count pairs which distance is <= dist
            pairs = 0
            while l < len(nums) or r < len(nums):
                # fast
                while r < len(nums) and nums[r] - nums[l] <= dist:
                    r += 1
                # count pairs in [l:r]
                pairs += r - l - 1
                l += 1
            return pairs >= k
            # sort items to count pairs with distance <= mid

        nums.sort()
        lo = 0
        hi = max(nums) - min(nums)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if feasible(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo

sol = Solution()
print(sol.smallDistancePair([0, 0, 0, 0, 1, 1, 1, 2, 2, 2], k = 20))