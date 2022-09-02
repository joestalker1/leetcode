class Solution:
    def validSubarraySize(self, nums, threshold: int) -> int:
        if not nums:
            return -1
        st = []
        prev = [-1 for i in range(len(nums))]
        nxt = [len(nums) for i in range(len(nums))]
        #keep increasing order
        for i in range(len(nums)):
            while st and nums[st[-1]] > nums[i]:
                j = st.pop()
                nxt[j] = i
            st.append(i)
        st = []
        for i in range(len(nums) - 1, -1, -1):
            while st and nums[i] < nums[st[-1]]:
                j = st.pop()
                prev[j] = i
            st.append(i)
        for i in range(len(nums)):
            left = prev[i]
            right = nxt[i]
            k = right - left - 1
            if threshold /k < nums[i]:
                return k
        return -1