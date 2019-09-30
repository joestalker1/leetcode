class Solution:
    def minimumAbsDifference(self, arr):
        if not arr or len(arr) < 2:
            return []
        if len(arr) == 2:
            return [arr[0], arr[1]] if arr[0] <= arr[1] else [arr[1], arr[0]]

        arr.sort()
        min_diff = float('inf')
        for i in range(1, len(arr)):
            diff = abs(arr[i] - arr[i-1])
            min_diff = min(min_diff, diff)
        res = []
        for i in range(1, len(arr)):
            diff = abs(arr[i] - arr[i-1])
            if min_diff == diff:
                res.append([arr[i-1], arr[i]])
        return res

sol = Solution()
print(sol.minimumAbsDifference([3,8,-10,23,19,-4,-14,27]))
print(sol.minimumAbsDifference([1,3,6,10,15]))
print(sol.minimumAbsDifference([4,2,1,3]))

