from collections import Counter

class Solution:
    def reductionOperations(self, nums) -> int:
        if not nums:
            return 0
        # uniq numbers
        # get frequency of every number
        freq = Counter(nums)
        if len(freq) == 1:
            # if number is on,there is no
            return 0
        # sort in asceding order
        uniq_nums = list(freq)
        uniq_nums.sort()
        # go from max value to min one and count numbers are less thsn current one
        total = 0
        step = 0
        for i in range(len(uniq_nums) - 1, 0, -1):
            step += freq[uniq_nums[i]]
            total += step
        return total