class Solution:
    def findMissingRanges(self, nums, lower: int, upper: int):
        if not nums:
            return None
        new_nums = nums[::]
        new_nums.insert(0, lower)
        new_nums.append(upper)
        ranges = []
        for i in range(1, len(new_nums)):
            if new_nums[i] - new_nums[i-1] > 1:
                a = new_nums[i-1]+1
                b = new_nums[i] - 1
                if a == b:
                    ranges.append(str(a))
                else:
                    ranges.append('{}->{}'.format(a, b))
        return ranges
