class Solution:
    def nextGreaterElement(self, nums1, nums2):
        st = []
        right = {a:-1 for a in nums1}
        for i in range(len(nums2) - 1, -1, -1):
            while st and st[-1] <= nums2[i]:
                st.pop()
            if st and nums2[i] in right:
                right[nums2[i]] = st[-1]
            st.append(nums2[i])
        res = []

        for a in nums1:
            res.append(right[a])
        return res


sol = Solution()
print(sol.nextGreaterElement([1,3,5,2,4], [6,5,4,3,2,1,7]))
print(sol.nextGreaterElement(nums1 = [4,1,2], nums2 = [1,3,4,2]))
