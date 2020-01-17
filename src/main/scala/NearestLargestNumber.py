class Solution:
    def nearest(self,arr, i):
        for j in range(len(arr)):
            low = i - j
            hi = i + j
            if 0 <= low and arr[low] > arr[i]:
                return low
            if hi < len(arr) and arr[hi] > arr[i]:
                return hi

    def find(self, arr, i):
        cache = [None for _ in range(len(arr))]
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                cache[j+1] = j
            elif arr[j+1] > arr[j]:
                cache[j] = j + 1

        for j,val in enumerate(cache):
            if val is None:
                cache[j] = self.nearest(arr, j)
        return cache[i]

sol = Solution()
print(sol.find([4, 1, 3, 5, 6], 0))



