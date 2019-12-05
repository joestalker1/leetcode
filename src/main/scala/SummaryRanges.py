class Solution(object):
    def summaryRanges(self, nums):
        if not nums:
            return []
        left = 0
        right = 0
        res = []
        for i in range(1, len(nums)):
            if nums[right] + 1 == nums[i]:
                right += 1
            else:
                if left < right:
                    res.append('{}->{}'.format(nums[left], nums[right]))
                else:
                    res.append(nums[left])
                left = i
                right = i
        if left < right:
            res.append('{}->{}'.format(nums[left], nums[right]))
        else:
            res.append(nums[left])
        return res



