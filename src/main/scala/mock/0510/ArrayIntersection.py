class Solution:
    def intersect(self, nums1, nums2):
        if not nums1 or not nums2:
            return []
        nums1.sort()
        nums2.sort()
        i = 0
        j = 0
        res = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                while i < len(nums1) and j < len(nums2) and nums1[i] == nums2[j]:
                    res.append(nums1[i])
                    i += 1
                    j += 1
            elif nums1[i] < nums2[j]:
                a = nums1[i]
                while i < len(nums1) and nums1[i] == a:
                    i += 1
            else:
                a = nums2[i]
                while i < len(nums2) and nums2[j] == a:
                    j += 1
        return res


sol = Solution()
print(sol.intersect(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))
print(sol.intersect(nums1 = [1,2,2,1], nums2 = [2,2]))





