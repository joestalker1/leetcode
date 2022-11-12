class Solution:
    def twoOutOfThree(self, nums1, nums2, nums3):
        num_set1 = set()
        for num in nums1:
            num_set1.add(num)
        num_set2 = set()
        for num in nums2:
            num_set2.add(num)
        num_set3 = set()
        for num in nums3:
            num_set3.add(num)
        set1 = num_set1.intersection(num_set2)
        set2 = num_set2.intersection(num_set3)
        set3 = num_set1.intersection(num_set3)
        return set1.union(set2).union(set3)


sol = Solution()
print(sol.twoOutOfThree([3,1],[2,3],[1,2]))