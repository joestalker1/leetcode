class Solution:
    def minMoves2(self, nums: List[int]):
        return self._minMoves2(nums)

    def _minMoves2(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        nums.sort()
        m = len(nums) // 2
        median = nums[m]
        return sum([abs(median - num) for num in nums])
