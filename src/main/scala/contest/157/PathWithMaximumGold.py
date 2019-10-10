class Solution:
    def getMaximumGold(self, grid):
        if not grid or len(grid[0]) == 0:
            return 0

        def grab(i, j, seen):
            #top
            max_gold = 0
            if i - 1 >= 0 and (i - 1, j) not in seen:
                seen.add((i - 1, j))
                max_gold = max(max_gold, grid[i-1][j] + grab(i - 1, j, seen))
                seen.remove((i-1, j))





