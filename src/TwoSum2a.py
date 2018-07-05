class Solution:
    def twoSum(self, nums, target):
        if not nums:
            return []
        map = {}
        for i in range(len(nums)):
            r = target - nums[i]
            if r in map.keys():
                return [map[r], i]
            map[nums[i]] = i
        return []