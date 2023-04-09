from math

class Solution:
    def minimizeSum(self, nums) -> int:
        if len(nums) < 4:
            return 0
        #remove max two numbers
        #remove min two numbers
        #remove max and min numbers
        #l1,l2,l3 ..... s3,s2,,s1
        s1 = s2 = s3 = 0
        l1 = l2 = l3 = math.inf
        for num in nums:
            if num > s1:
                s3 = s2
                s2 = s1
                s1 = num
            elif num > s2:
                s3 = s2
                s2 = num
            elif num > s3:
                s3 = num
            if num < l1:
                l3 = l2
                l2 = l1
                l1 = num
            elif num < l2:
                l3 = l2
                l2 = num
            elif num < l3:
                l3 = num
        return min(s3-l1,s1-l3,s2-l2)