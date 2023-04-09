class Solution:
    def minOperations(self, nums):
        # assert self._minOperations([1]) == 0, 'test1'
        # assert self._minOperations([1,2,3]) == 0, 'test2'
        # assert self._minOperations([3,2,1]) == 6, 'test3'
        # assert self._minOperations([1,3,1]) == 3, 'test4'
        return self._minOperations(nums)
   lma = a*b/ gcd(a,b) ,
   3 * b/
    def _minOperations(self, nums):
        if not nums:
            return 0
        oper_num = 0
        last = 0
        for i in range(len(nums)):
            if last < nums[i]:
                last = nums[i]
                continue
            oper_num += last - nums[i] + 1
            last += 1
        return oper_num