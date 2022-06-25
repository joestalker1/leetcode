class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:

        def dfs(land, r, c):
            if r == row or c == col or land[r][c] == 1:
                return False
            if r == row - 1 and land[r][c] == 0:
                return True
            land[r][c] = 1
            if r - 1 >= 0 and land[r - 1][c] == 0:
                if dfs(land, r - 1, c):
                    return True
            if c - 1 >= 0 and land[r][c - 1] == 0:
                if dfs(land, r, c - 1):
                    return True
            if c + 1 < col and land[r][c + 1] == 0:
                if dfs(land, r, c + 1):
                    return True
            if r + 1 < row and land[r + 1][c] == 0:
                if dfs(land, r + 1, c):
                    return True
            return False

        lo = 1
        hi = len(cells)
        max_day = 0
        while lo <= hi:
            land = [[0] * col for _ in range(row)]
            m = lo + (hi - lo) // 2
            for i in range(m):
                r, c = cells[i]
                land[r - 1][c - 1] = 1
            can_go = False
            for c in range(col):
                if dfs(land, 0, c):
                    can_go = True
                    break
            if can_go:
                max_day = m
                lo = m + 1
            else:
                hi = m - 1
        return max_day


sol = Solution()
print(sol.latestDayToCross(6,2,[[4,2],[6,2],[2,1],[4,1],[6,1],[3,1],[2,2],[3,2],[1,1],[5,1],[5,2],[1,2]]))#3
print(sol.latestDayToCross(2,2,[[1,1],[2,1],[1,2],[2,2]]))#2