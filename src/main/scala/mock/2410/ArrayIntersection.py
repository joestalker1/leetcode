class Solution:
    def intersection(self, nums1, nums2):
        if not nums1 or not nums2:
            return []
        nums1.sort()
        nums2.sort()
        i = 0
        j = 0
        res = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                if len(res) == 0:
                    res.append(nums1[i])
                elif res[-1] != nums1[i]:
                    res.append(nums1[i])
                i += 1
                j += 1
        return res

sol = Solution()
print(sol.intersection(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))
print(sol.intersection(nums1 = [1,2,2,1], nums2 = [2,2]))


