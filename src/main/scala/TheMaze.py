class Solution:
    def hasPath(self, maze, start, dest):
        if not maze or not start or not dest:
            return False
        visited = [[False] * len(maze[0]) for _ in range(len(maze))]

        def dfs(r,c):
            visited[r][c] = True
            if [r,c] == dest:
                return True
            for dr,dc in [[1,0],[-1,0],[0,-1], [0,1]]:
                r1 = r + dr
                c1 = c + dc
                while 0<= r1 < len(maze) and 0 <= c1 < len(maze[0]) and maze[r1][c1] == 0:
                    r1 = r1 + dr
                    c1 = c1 + dc
                r1 -= dr
                c1 -= dc
                if not visited[r1][c1]:
                    if dfs(r1,c1):
                        return True
            return False

        dfs(start[0], start[1])
        return visited[dest[0]][dest[1]]



