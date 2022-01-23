class Solution:
    def maxSumMinProduct(self, nums) -> int:
        # assert self._maxSumMinProduct([1,2,2]) == 8,'test1'
        # assert self._maxSumMinProduct([1,1,1]) == 3,'test2'
        # assert self._maxSumMinProduct([1,2,3]) == 10,'test3'
        return self._maxSumMinProduct(nums)

    def _maxSumMinProduct(self, nums):
        MOD = 10 ** 9 + 7
        # prefix sum
        pr = [0]
        for i in range(len(nums)):
            pr.append(pr[-1] + nums[i])
        st = []
        max_prod = 0
        # keep increasing order in stack
        for i in range(len(nums) + 1):
            # if we meet nums[i] < stack[-1],let count max array product
            while st and (i == len(nums) or nums[st[-1]] > nums[i]):
                j = st.pop()
                # nums[j] is min value for all items are to the right of nums[j]
                max_prod = max(max_prod, nums[j] * (pr[i] - pr[st[-1] + 1 if st else 0]))
            st.append(i)
        return max_prod % MOD

def testMaxSumMinProduct(nums):
    if not nums:
        return 0
    max_prod = 0
    for start in range(len(nums)):
        for end in range(start, len(nums)):
            min_val = nums[start]
            cur_sum = 0
            for i in range(start, end+1):
                cur_sum += nums[i]
                min_val = min(min_val, nums[i])
            max_prod = max(max_prod, min_val * cur_sum)
            if min_val * cur_sum == 156:
                print('{}-{}'.format(start,end))
    return max_prod




print(testMaxSumMinProduct([1,2,3,2]))#14
print(testMaxSumMinProduct([5,10,6,10,4,2,1,4,5,2,4,2,7,5,8,6,3,6,6,4]))#156
sol = Solution()
print(sol.maxSumMinProduct([5,10,6,10,4,2,1,4,5,2,4,2,7,5,8,6,3,6,6,4]))#156


