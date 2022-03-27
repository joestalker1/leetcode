class Solution:
    def digArtifacts(self, n: int, artifacts, dig) -> int:
        grid = [[-2] *n for _ in range(len(artifacts))]
        for i in range(len(artifacts)):
            # (0,1) - (1,1)
            r1, c1, r2, c2 = artifacts[i]
            for r in range(r1,r2+1):
                for c in range(c1,c2+1):
                    grid[r][c] = i
        loot = set()
        for r,c in dig:
            grid[r][c] = -1
        for r in range(n):
            for c in range(n):
                if grid[r][c] != -1 and grid[r][c] != -2:
                    loot.add(grid[r][c])
        return len(artifacts) - len(loot)


sol = Solution()
print(sol.digArtifacts(5,[[3,1,4,1],[1,1,2,2],[1,0,2,0],[4,3,4,4],[0,3,1,4],[2,3,3,4]],[[0,0],[2,1],[2,0],[2,3],[4,3],[2,4],[4,1],[0,2],[4,0],[3,1],[1,2],[1,3],[3,2]]))
print(sol.digArtifacts(n = 2, artifacts = [[0,0,0,0],[0,1,1,1]], dig = [[0,0],[0,1],[1,1]]))#2
print(sol.digArtifacts(n = 2, artifacts = [[0,0,0,0],[0,1,1,1]], dig = [[0,0],[0,1]]))#1