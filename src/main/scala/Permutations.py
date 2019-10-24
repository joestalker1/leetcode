class Solution:
    def perm(self, arr):
        if not arr:
            return arr

        def run_perm(i, res):
            if i == len(arr):
                res.append(arr[:])
                return
            for j in range(i, len(arr)):
                arr[i],arr[j] = arr[j],arr[i]
                run_perm(i + 1, res)
                arr[i], arr[j] = arr[j], arr[i]

        res = []
        run_perm(0, res)
        return res

sol = Solution()
print(sol.perm([1,2,3]))




