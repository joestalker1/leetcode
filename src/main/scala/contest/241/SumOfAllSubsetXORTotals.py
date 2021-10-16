class Solution:
    def subsetXORSum(self, nums) -> int:
        if not nums:
            return 0

        def create_subset(i, buf):
            if i == len(nums):
                #calculate xor
                xor = 0
                for a in buf:
                    xor ^= a
                return xor
            xor_total = create_subset(i+1, buf)
            return xor_total + create_subset(i+1, buf + [nums[i]])

        return create_subset(0, [])


sol = Solution()
print(sol.subsetXORSum([5,1,6]))#28