class Solution:
    def numRollsToTarget(self, d, f, target):
        if d == 0:
            return 0
        ways = 0
        def calc_sum(dice, sum_so_far):
            nonlocal ways
            if dice == d:
                if sum_so_far == target:
                    ways += 1
                return
            for j in range(1,f + 1):
                calc_sum(dice + 1, sum_so_far + j)

        calc_sum(0, 0)
        return ways % (10 ** 9 + 7)


sol = Solution()
print(sol.numRollsToTarget(d = 30, f = 30, target = 500))
print(sol.numRollsToTarget(d = 1, f = 2, target = 3))
print(sol.numRollsToTarget(d = 2, f = 5, target = 10))
print(sol.numRollsToTarget(d = 2, f = 6, target = 7))
print(sol.numRollsToTarget(d = 1, f = 6, target = 3))


