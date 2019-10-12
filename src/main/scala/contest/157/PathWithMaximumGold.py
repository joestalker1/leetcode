class Solution:
    def getMaximumGold(self, grid):
        if not grid or len(grid[0]) == 0:
            return 0

        def grab(i, j):
            if i < 0 or i == len(grid) or j < 0 or j == len(grid[0]) or grid[i][j] == 0:
                return 0
            g = grid[i][j]
            grid[i][j] = 0
            max_gold = g
            if i - 1 >= 0:
                max_gold = max(max_gold, g + grab(i - 1, j))
            if i + 1 < len(grid):
                max_gold = max(max_gold, g + grab(i + 1, j))
            if j + 1 < len(grid[0]):
                max_gold = max(max_gold, g + grab(i, j + 1))
            if j - 1 >= 0:
                max_gold = max(max_gold, g + grab(i, j - 1))
            grid[i][j] = g
            return max_gold

        gold = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                gold = max(gold, grab(x, y))
        return gold

sol = Solution()
print(sol.getMaximumGold([[0,0,19,5,8],[11,20,14,1,0],[0,0,1,1,1],[0,2,0,2,0]]))#77
print(sol.getMaximumGold([[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]))
print(sol.getMaximumGold([[0,6,0],[5,8,7],[0,9,0]]))

