class Solution:
    def nextGreaterElement(self, nums1, nums2):
        if not nums1 and not nums2:
            return []
        if not nums1:
            return []
        if not nums2:
            return [-1]*len(nums1)

        st = []
        m = {}
        for i,a in enumerate(nums2):
            while st and st[-1] < a:
                m[st[-1]] = a
                st.pop()
            st.append(a)
        res = [-1] * len(nums1)
        for i in range(len(nums1)):
            if nums1[i] in m:
                res[i] = m[nums1[i]]
        return res


sol = Solution()
print(sol.nextGreaterElement([4,1,2], [1,2,3,4]))#[-1,2,3]
print(sol.nextGreaterElement(nums1 = [4,1,2], nums2 = [1,3,4,2]))#[-1,3,-1]
print(sol.nextGreaterElement(nums1 = [2,4], nums2 = [1,2,3,4]))#[3,-1]


