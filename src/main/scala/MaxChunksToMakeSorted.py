class Solution:
    def maxChunksToSorted(self, arr):
        if not arr:
            return 0
        ans = 0
        max_val = 0
        for i in range(len(arr)):
            max_val = max(max_val, arr[i])
            if max_val == i:
                ans += 1
        return ans


sol = Solution()
print(sol.maxChunksToSorted([2,0,1]))#1
print(sol.maxChunksToSorted([0,1]))#2
print(sol.maxChunksToSorted([0,2,1]))#2
print(sol.maxChunksToSorted([0]))#1
print(sol.maxChunksToSorted([1,0,2,3,4]))#4
print(sol.maxChunksToSorted([4,3,2,1,0]))#1