class Solution:
    def dfs(self, numCourses, courses, node, i, path):
        if numCourses == path:
            return path
        max_path = path
        for j in range(i, len(courses)):
            e, s = courses[j]
            if s == node or node == -1:
                if node == -1:
                    path = 1
                path = self.dfs(numCourses, courses, e, j + 1, path + 1)
                max_path = max(max_path, path)
        return path

    def canFinish(self, numCourses, prerequisites):
        if not prerequisites or numCourses == 0:
            return False
        path = self.dfs(numCourses, prerequisites, -1, 0, 0)
        return path == numCourses

sol = Solution()
print(sol.canFinish(4, [[1,0],[0,2], [2,3]]))
#print(sol.canFinish(2, [[1,0],[0,1]]))
#print(sol.canFinish(2, [[1,0]]))
