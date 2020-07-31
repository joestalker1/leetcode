from collections import defaultdict


class Solution:
    def gardenNoAdj(self, N, paths):
        ans = [0] * N
        adj_list = defaultdict(list)
        for x, y in paths:
            adj_list[x].append(y)
            adj_list[y].append(x)

        for i in range(1, N + 1):
            clr = [0] * 4
            for x in adj_list[i]:
                clr[ans[x-1]] = 1

            for j in range(1,5):
                if clr[j] == 0:
                    ans[i-1] = j
                    break
        return ans

sol = Solution()
arr = [[1,2]]
print(sol.gardenNoAdj(5, []))