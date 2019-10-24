class Solution:
    def comb(self, arr):
        if not arr:
            return []

        def all_comb(i, res, cur):
            if i == len(arr):
                res.append(cur)
            else:
                all_comb(i + 1, res, cur)
                new_cur = cur[:]
                new_cur.append(arr[i])
                all_comb(i + 1, res, new_cur)
        res = []
        all_comb(0, res, [])
        return res

sol = Solution()
print(sol.comb([1,2,3]))