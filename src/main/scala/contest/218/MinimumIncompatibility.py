import math

class Solution:
    def minimumIncompatibility(self, nums, k):
        n = len(nums)
        m = []
        for i in range(k):
            m.append(set())

        self.min = math.inf

        def calc_impact(s, num):
            if len(s) == 0:
                return 0
            if len(s) == 1:
                return abs(num - list(s)[0])
            min_val = min(s)
            max_val = max(s)
            if num < min_val:
                return min_val - num
            if num > max_val:
                return num - max_val
            return 0

        bucket_size = n // k

        def calc_incompatibility(m):
            total = 0
            for s in m:
                min_val = min(s)
                max_val = max(s)
                total += (max_val - min_val)
            return total

        def backtrack(cur, m, acc):
            if cur >= n:
                self.min = min(acc, self.min)
                return
            visited = set()
            for s in m:
                if nums[cur] in s or len(s) == bucket_size or tuple(s) in visited:
                    continue
                impact = calc_impact(s, nums[cur])
                if acc + impact < self.min:
                    s.add(nums[cur])
                    backtrack(cur + 1, m, acc + impact)
                    s.discard(nums[cur])
                visited.add(tuple(s))

        backtrack(0, m, 0)
        return self.min if self.min != math.inf else -1


sol = Solution()
print(sol.minimumIncompatibility([12,5,16,7,13,4,3,14,4,11,8,6,6,1,15,12], 4))#17
print(sol.minimumIncompatibility([10,4,4,2,11,10,8,9,1,2,2,10], 4))
# print(sol.minimumIncompatibility([7,3,16,15,1,13,1,2,14,5,3,10,6,2,7,15], 8))
# print(sol.minimumIncompatibility([5,3,3,6,3,3], 3))# -1
# print(sol.minimumIncompatibility([6,3,8,1,3,1,2,2], 4))
print(sol.minimumIncompatibility([1,2,1,4],2))








