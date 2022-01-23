class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:

        def dfs(seen, cur_island, orig_x, orig_y, x, y):
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
                return
            if (x, y) in seen or not grid[x][y]:
                return
            cur_island.add((x - orig_x, y - orig_y))
            seen.add((x, y))
            dfs(seen, cur_island, orig_x, orig_y, x + 1, y)
            dfs(seen, cur_island, orig_x, orig_y, x, y + 1)
            dfs(seen, cur_island, orig_x, orig_y, x - 1, y)
            dfs(seen, cur_island, orig_x, orig_y, x, y - 1)

        uniq_islands = set()
        seen = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                cur_island = set()
                dfs(seen, cur_island, i, j, i, j)
                if cur_island:
                    uniq_islands.add(frozenset(cur_island))
        return len(uniq_islands)
