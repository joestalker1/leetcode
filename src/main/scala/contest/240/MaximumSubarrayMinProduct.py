class Solution:
    def maxSumMinProduct(self, nums) -> int:
        # assert self._maxSumMinProduct([1,2,2]) == 8,'test1'
        # assert self._maxSumMinProduct([1,1,1]) == 3,'test2'
        # assert self._maxSumMinProduct([1,2,3]) == 10,'test3'
        return self._maxSumMinProduct(nums)

    def _maxSumMinProduct(self, nums):
        left_min = [-1 for _ in range(len(nums))]
        right_min = [len(nums) for i in range(len(nums))]
        # keep up increasing order to find closest left min item
        pr = [0]
        for i in range(len(nums)):
            pr.append(pr[-1] + nums[i])
        st = []
        for i in range(len(nums)):
            while st and nums[st[-1]] >= nums[i]:
                st.pop()
            if st:
                left_min[i] = st[-1]
            st.append(i)
        # keep up increasing order to find closest right min item
        st = []
        for i in range(len(nums)):
            while st and nums[st[-1]] > nums[i]:
                right_min[st[-1]] = i
                st.pop()
            st.append(i)
        min_prod = pr[-1] * min(nums)
        for i in range(len(nums)):
            s = left_min[i] + 1
            e = right_min[i] - 1
            min_prod = max(min_prod, nums[i] * (pr[e + 1] - pr[s]))
        return min_prod % (10 ** 9 + 7)


class BestSolution:
    def maxSumMinProduct(self, nums) -> int:
        # assert self._maxSumMinProduct([1,2,2]) == 8,'test1'
        # assert self._maxSumMinProduct([1,1,1]) == 3,'test2'
        # assert self._maxSumMinProduct([1,2,3]) == 10,'test3'
        return self._maxSumMinProduct(nums)

    def _maxSumMinProduct(self, nums):
        MOD = 10 ** 9 + 7
        # keep up increasing order to find closest left min item
        pr = [0]
        for i in range(len(nums)):
            pr.append(pr[-1] + nums[i])
        st = []
        max_prod = 0
        for i in range(len(nums) + 1):
            while st and (i == len(nums) or nums[st[-1]] > nums[i]):
                # leftmos min item
                # subarray from [st.pop+1: i)
                # min item is at [j]
                # if st is empty we take pr[st.pop+1] - st[0]
                j = st.pop()
                print('{}-{}:{}'.format((st[-1] + 1 if st else 0), i, j))
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


