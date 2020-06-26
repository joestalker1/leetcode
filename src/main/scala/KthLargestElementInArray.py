class Solution:
    def findKthLargest(self, nums, K):
        if not nums or K > len(nums):
            return None

        def parition(s, e):
            i = s
            x = nums[e]
            for j in range(s, e):
                if nums[j] > x:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[e], nums[i] = nums[i], nums[e]
            return i

        def quick_select(s, e, k):
            if 0 < k <= e - s + 1:
                p = parition(s, e)
                if p - s + 1 == k:
                    return nums[p]#<<<<<----
                if p - s + 1 > k:
                    return quick_select(s, p - 1, k)
                return quick_select(p + 1, e, k - p + s - 1)

        return quick_select(0, len(nums) - 1, K)


sol = Solution()
print(sol.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  # 4
print(sol.findKthLargest([3, 2, 1, 5, 6, 4], 2))
