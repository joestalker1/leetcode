class Solution:
    def canVisitAllRooms(self, rooms):
        if not rooms or len(rooms) == 0:
            return False
        def dfs(room, visited):
            visited.add(room)
            for key in rooms[room]:
                if key in visited:
                    continue
                dfs(key, visited)
        visited = set()
        dfs(0, visited)
        return len(visited) == len(rooms)


sol = Solution()
print(sol.canVisitAllRooms([[1],[],[0,3],[1]]))#false
print(sol.canVisitAllRooms([[1],[2],[3],[]]))#true
print(sol.canVisitAllRooms([[1,3],[3,0,1],[2],[0]]))#false