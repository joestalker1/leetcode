class Solution:
    def wiggleMaxLength(self, nums) -> int:
        # assert self._wiggleMaxLength([1,1,1]) == 1, 'test1'
        # assert self._wiggleMaxLength([1,2,1]) == 3, 'test2'
        # assert self._wiggleMaxLength([1,3,4,1]) == 3, 'test3'
        # assert self._wiggleMaxLength([4,3,1,2]) == 3, 'test4'
        return self._wiggleMaxLength(nums)

    def _wiggleMaxLength(self, nums) -> int:
        if not nums:
            return 0
        up = 1
        down = 1
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] > 0:
                up = down + 1
            elif nums[i] - nums[i - 1] < 0:
                down = up + 1
        return max(up, down)