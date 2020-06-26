class Solution:
    def permutations(self, arr):
        if not arr:
            return

        def perm(l, r, res):
            if l == r:
                res.append(arr[::])
                return
            for i in range(l, r + 1):
                arr[i],arr[l] = arr[l],arr[i]
                perm(l+1, r, res)
                arr[i], arr[l] = arr[l], arr[i]
        res = []
        perm(0, len(arr) - 1, res)
        return res


sol = Solution()
print(sol.permutations([1, 2, 3, 4]))
