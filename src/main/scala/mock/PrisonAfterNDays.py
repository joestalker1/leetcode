class Solution(object):
    def prisonAfterNDays(self, cells, N):
        if not cells or not N:
            return cells
        cur = cells
        cp = [0] * 8
        for d in range(N):
            None
            # print("{} day {}".format(d, cur))
            # j = 0
            # while j < 6:
            #     if cur[j] == cur[j + 2]:
            #         cp[j + 1] = 1
            #     else:
            #         cp[j + 1] = 0
            #     j += 1
            # cur[7] = 0
            # cur[0] = 0
            # t = cur
            # cur = cp
            # cp = t
        return cur


sol = Solution()
print(sol.prisonAfterNDays([1,0,0,1,0,0,1,0], 1000000000))
#print(sol.prisonAfterNDays([0, 1, 0, 1, 1, 0, 0, 1], 100000))
