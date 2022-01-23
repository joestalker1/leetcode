class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        i = 0
        j = 0
        end = len(nums1) - 1
        # compare items from the end of nums1 and nums2,put max item to the end of nums1
        while end >= 0:
            if j == n or i < m and j < n and nums1[m-i-1] > nums2[n-j-1]:
                nums1[end] = nums1[m-i-1]
                i += 1
            elif i == m or i < m and j < n and nums1[m-i-1] <= nums2[n-j-1]:
                nums1[end] = nums2[n - j - 1]
                j += 1
            end -= 1

s1 = set([1,2,3])
s2 = set([1,2])
print(s1 | s2)