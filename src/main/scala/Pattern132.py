class Solution:
    def find132pattern(self, nums):
        if not nums:
            return False
        left = [0] * len(nums)
        left[0] = nums[0]
        for i in range(1, len(nums)):
            left[i] = min(left[i - 1], nums[i])
        st = []
        for i in range(len(nums) - 1, -1, -1):
            if i and nums[i] <= left[i]:
                continue
            # keep increasing subsequence
            while st and nums[i] > nums[st[-1]]:
                k = st.pop()
                if left[i] < nums[k]:
                    return True
            st.append(i)
        return False
