class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        if numCourses == 0:
            return []
        adj_list = [[] for i in range(numCourses)]

        # [a,b] b goes first, a -> b
        for a,b in prerequisites:
            adj_list[b].append(a)

        def top_sort_if_no_cycle(node, rec_stack, seen, res):
            seen.add(node)
            rec_stack[node] = True
            for child in adj_list[node]:
                if child not in seen:
                    if top_sort_if_no_cycle(child, rec_stack, seen, res):
                        return True
                elif rec_stack[child]:
                    return True
            res.append(node)
            rec_stack[node] = False
            return False

        rec_stack = [False] * numCourses
        res = []
        seen = set()
        for n in range(numCourses):
            if n not in seen:
                if top_sort_if_no_cycle(n, rec_stack, seen, res):
                    return []
        return res[::-1]


sol = Solution()
print(sol.findOrder(2, [[0,1],[1,0]]))
print(sol.findOrder(1,[]))
print(sol.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
print(sol.findOrder(2, [[1,0]] ))