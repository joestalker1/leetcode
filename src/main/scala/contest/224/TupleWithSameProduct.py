from collections import defaultdict

class Solution:
    def tupleSameProduct(self, nums):
        m = defaultdict(int)
        tuples = 0
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                #calculate the product
                product = nums[i] * nums[j]
                # if we meet this product earlier,let count them as 8 cases
                if product in m:
                    tuples += (8 * m[product])
                #increase count of this product
                m[product] += 1
        return tuples




