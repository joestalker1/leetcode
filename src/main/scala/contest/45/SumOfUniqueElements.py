from collections import Counter

class Solution:
    def sumOfUnique(self, nums):
        numbers = Counter(nums)
        sum_num = 0
        for num in numbers:
            if numbers[num] == 1:
                sum_num += num
        return sum_num