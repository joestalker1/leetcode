class Solution:
    def findLHS(self, nums):
        freq = {}
        max_len = 0
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] in freq:
                c = freq[nums[i]]
                freq[nums[i]] = c + 1
            else:
                freq[nums[i]] = 1
            min1 = nums[i]
            max1 = min1 + 1
            len1 = 0
            if max1 in freq:
               c1 = freq[max1]
               c2 = freq[min1]
               len1 = c1 + c2
            max1 = nums[i]
            min1 = max1 - 1
            len2 = 0
            if min1 in freq:
               c1 = freq[max1]
               c2 = freq[min1]
               len2 = c1 + c2
            len1 = max(len1, len2)
            max_len = max(len1, max_len)
        return max_len

sol = Solution()
print(sol.findLHS([1,3,2,2,5,2,3,7]))



