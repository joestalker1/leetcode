class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

class Solution:
    def cloneGraph(self, node):
        if not node:
            return None
        cache = {}

        def dfs(n):
            new_node = Node(n.val, [])
            cache[new_node.val] = new_node
            for neighbor in n.neighbors:
                if neighbor.val in cache:
                    new_node.neighbors.append(cache[neighbor.val])
                else:
                    new_node.neighbors.append(dfs(neighbor))
            return new_node
        return dfs(node)

