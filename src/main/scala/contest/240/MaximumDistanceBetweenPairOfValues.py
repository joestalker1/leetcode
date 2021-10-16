class Solution:
    def maxDistance(self, nums1, nums2):
        # assert self._maxDistance([1, 2, 3], [1, 2, 3]) == 2, 'test0'
        # assert self._maxDistance([1, 2, 3], [3, 2, 1]) == 2, 'test1'
        # assert self._maxDistance([], [1, 2, 3]) == 0, 'test3'
        return self._maxDistance(nums1, nums2)

    def _maxDistance(self, nums1, nums2):
        if not nums1 or not nums2:
            return 0
        i = 0
        j = 0
        max_dist = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                i += 1
            else:
                max_dist = max(max_dist,j - i)
                j += 1
        return max_dist


sol = Solution()
print(sol.maxDistance(nums1 = [2,2,2], nums2 = [10,10,1]))#1
print(sol.maxDistance([30,29,19,5], nums2 = [25,25,25,25,25]))
print(sol.maxDistance(nums1 = [55,30,5,4,2], nums2 = [100,20,10,10,5]))#2