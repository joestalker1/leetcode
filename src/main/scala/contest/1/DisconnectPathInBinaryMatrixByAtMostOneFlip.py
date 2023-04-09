from collections import defaultdict

class Solution:

    def isPossibleToCutPath(self, grid) -> bool:
        n = len(grid)
        m = len(grid[0])

        def dfs(r,c,cur_path,vert_cnt):
            if r == n - 1 and c == m - 1:
                for r1,c1 in cur_path:
                    vert_cnt[(r1,c1)] += 1
                return
            #go to bottom
            if r + 1 < n and grid[r+1][c] == 1:
                dfs(r+1,c,cur_path +[[r+1,c]],vert_cnt)
            # go to the right:
            if c + 1 < m and grid[r][c+1] == 1:
                dfs(r,c+1,cur_path + [[r,c+1]], vert_cnt)

        vert_cnt = defaultdict(int)
        dfs(0, 0,[], vert_cnt)
        if vert_cnt[(n-1,m-1)] < 2:
            return True
        disconected = False
        for i in range(n):
            if disconected:
                break
            for j in range(m):
                if vert_cnt[(i,j)] == 1:
                    disconected = True
                    break
        return disconected




sol = Solution()
print(sol.isPossibleToCutPath([[1,1,1],[1,0,0],[1,1,1]]))#true
print(sol.isPossibleToCutPath([[1,0,1],[0,0,1],[1,1,1]]))#true