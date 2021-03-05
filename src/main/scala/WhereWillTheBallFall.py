class Solution:
    def findBall(self, grid):
        if not grid or len(grid[0]) <= 1:
            return [-1] * len(grid)
        # row number
        n = len(grid)
        # column number
        m = len(grid[0])
        answer = [-1] * m
        # 1 from left to right
        # -1 from right to left
        for i in range(m):
            c = i
            r = 0
            while r < n:
                if grid[r][c] == -1:
                    if c == 0 or (c-1) >= 0 and grid[r][c-1] == 1:
                        break
                    c -= 1
                else:
                    if c == m - 1 or c+1< m and grid[r][c+1] == -1:
                        break
                    c+=1
                r += 1
            if r == n:
                answer[i] = c
        return answer


sol = Solution()
#[0,1,2,3,4,-1]
print(sol.findBall(grid = [[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]))
# [1,-1,-1,-1,-1]
print(sol.findBall([[1, 1, 1, -1, -1], [1, 1, 1, -1, -1], [-1, -1, -1, 1, 1], [1, 1, 1, 1, -1], [-1, -1, -1, -1, -1]]))
