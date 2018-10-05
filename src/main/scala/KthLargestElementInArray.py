class Solution:
    def quick_select(self, arr, l, r, k):
        if 0 < k <= r - l + 1:
            pos = self.partition(arr, l, r)
            if pos - l == k - 1:
                return arr[pos]
            if pos - l > k - 1:
                return self.quick_select(arr, l, pos - 1, k)
            return self.quick_select(arr, pos + 1, r, k - pos + l - 1)

    def partition(self, arr, l, r):
        i = l
        x = arr[r]
        for j in range(l, r):
            if arr[j] > x:
                arr[i],arr[j] = arr[j],arr[i]
                i += 1
        arr[i], arr[r] = arr[r], arr[i]
        return i

    def findKthLargest(self, nums, k):
        return self.quick_select(nums, 0, len(nums) - 1, k)

sol = Solution()
print(sol.findKthLargest([3,2,1,5,6,4], 2))