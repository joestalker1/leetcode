class Solution:
    def compareVersion(self, version1, version2):
        if not version1 and not version2:
            return 0
        if not version1:
            return -1
        if not version2:
            return 1
        nums1 = version1.split('.')
        nums2 = version2.split('.')
        i = 0
        j = 0
        while i < len(nums1) or j < len(nums2):
            a = int(nums1[i]) if i < len(nums1) else 0
            b = int(nums2[j]) if j < len(nums2) else 0
            if a == b:
                i += 1
                j += 1
            else:
                return -1 if a < b else 1
        return 0

sol = Solution()
print(sol.compareVersion("1.0", "1"))
print(sol.compareVersion("0.1", "1.1"))
print(sol.compareVersion("1.0.1", "1"))
print(sol.compareVersion("7.5.2.4", "7.5.3"))