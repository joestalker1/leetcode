class Solution:
    def minOperations(self, nums1, nums2):
        if len(nums2) > 6 * len(nums1) or len(nums1) > 6 * len(nums2):
            return -1
        s1 = sum(nums1)
        s2 = sum(nums2)
        cnt = 0
        nums1.sort()
        nums2.sort()
        if s1 >= s2:
            nums1,nums2 = nums2,nums1
            s1,s2 = s2,s1
        #s2 > s1
        i = 0
        j = len(nums2) - 1

        while s2 > s1:
            if j < 0 or i < len(nums1) and (6 - nums1[i]) > (nums2[j] - 1):
                s1 += 6 - nums1[i]
                i += 1
            else:
                s1 += nums2[j] - 1
                j -= 1
            cnt += 1
        return cnt




