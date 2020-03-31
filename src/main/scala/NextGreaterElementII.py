class Solution:
    def nextGreaterElements(self, nums):
        if not nums:
            return []

        st = []
        res = [-1] * len(nums)
        for i in range(2 * len(nums) - 1,-1,-1):#2*n because we have to consider greater max from the left
            j = i % len(nums)
            num = nums[j]
            while st and nums[st[-1]] <= num: #pop items <= current item
                st.pop()
            if st:
                res[j] = nums[st[-1]]
            # add next greater for the next element
            st.append(j)
        return res


sol = Solution()
#print(sol.nextGreaterElements([1, 5, 3, 6, 8]))
#print(sol.nextGreaterElements([5, 4, 3, 2, 1]))
#print(sol.nextGreaterElements([3, 2, 1]))
print(sol.nextGreaterElements([1, 2, 1]))
