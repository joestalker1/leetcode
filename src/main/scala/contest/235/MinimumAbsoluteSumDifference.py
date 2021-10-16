import bisect

class Solution:
    def minAbsoluteSumDiff(self, nums1, nums2) -> int:
        sum_of_diff = 0
        gain = 0
        #maximize the difference between abs(nums1[i] - nums2[i]) and abs(other nums1[i] - nums2[i])
        sorted_nums1 = sorted(nums1)
        for i in range(len(nums1)):
            diff = abs(nums1[i] - nums2[i])
            sum_of_diff += diff
            if gain > diff:
                continue
            j = bisect.bisect_right(sorted_nums1, nums2[i])
            if j == len(nums1):
                j -= 1
            gain = max(gain, diff - abs(sorted_nums1[j] - nums2[i]))
            gain = max(gain, diff - abs(sorted_nums1[j-1] - nums2[i]))
        return (sum_of_diff - gain) % (10 ** 9 + 7)

sol = Solution()
print(sol.minAbsoluteSumDiff([1,28,21], [9,21,20]))#9
print(sol.minAbsoluteSumDiff([1,10,4,4,2,7],[9,3,5,1,7,4]))#20

