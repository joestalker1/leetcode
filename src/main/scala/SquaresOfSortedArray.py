class Solution:
    def sortedSquares(self, arr):
        if not arr:
            return []
        j = 0
        while j < len(arr) and arr[j] < 0:
            j += 1
        i = j - 1
        res = []
        while i >= 0 and j < len(arr):
            a = arr[i] ** 2
            b = arr[j] ** 2
            if a < b:
                res.append(a)
                i -= 1
            else:
                res.append(b)
                j += 1
        while i >= 0:
            res.append(arr[i] ** 2)
            i -= 1
        while j < len(arr):
            res.append(arr[j] ** 2)
            j += 1
        return res


sol = Solution()
print(sol.sortedSquares([-1]))
print(sol.sortedSquares([-4,-1,0,3,10]))






