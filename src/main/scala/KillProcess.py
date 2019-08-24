from collections import defaultdict

class Solution:
    def killProcess(self, pid, ppid, kill):
        if not pid or not ppid or not kill:
            return
        queue = [kill]
        res = []
        parent_to_child = defaultdict(lambda :[])
        for i in range(len(ppid)):
            parent_to_child[ppid[i]].append(pid[i])

        while len(queue) > 0:
            proc = queue.pop()
            res.append(proc)
            for child in parent_to_child[proc]:
                queue.append(child)
        return res


sol = Solution()
print(sol.killProcess([1, 3, 10, 5], [3, 0, 5, 3], 5))