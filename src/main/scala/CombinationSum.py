class Solution:
    def insert_if_new(self, res, cur):
        for l in res:
            if l == cur:
                return
        res.append(cur)

    def gen(self, from_i, candidates, target, res, cur):
        if sum(cur) == target:
            self.insert_if_new(res, cur)
            return
        if sum(cur) > target or from_i == len(candidates):
            return

        self.gen(from_i + 1, candidates, target, res, cur)
        cur1 = cur[:]
        cur1.append(candidates[from_i])
        self.gen(from_i, candidates, target, res, cur1)
        cur2 = cur1[:]
        self.gen(from_i + 1, candidates, target, res, cur2)

    def combinationSum(self, candidates, target):
        if not candidates:
            return []
        res = []
        self.gen(0, candidates, target, res, [])
        return res

sol = Solution()
print(sol.combinationSum([2,3,5], 8))
#print(sol.combinationSum([2,3,6,7], 7))