class Solution:
    def largestSubarray(self, nums, k: int):
        # assert self._largestSubarray( [1,4,5,2,3], 3) == [5,2,3],'test1'
        # assert self._largestSubarray( [1], 3) == [], 'test2'
        return self._largestSubarray(nums, k)

    def _largestSubarray(self, nums, k: int):
        if len(nums) < k:
            return []
        ind = 0
        j = 0
        # i is start of all k-digits numbers
        for i in range(1, len(nums) - k + 1):
            # position is inside k-digits number
            if j != 0:
                j -= 1
            # compare current and max numbers until theis digits are same
            while j < (k - 1) and nums[i + j] == nums[ind + j]:
                j += 1
            # if current number is greater max one,let update it.
            if nums[i + j] > nums[ind + j]:
                ind = i
        return nums[ind:ind + k]
