
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors



class Solution:
    def cloneGraph(self, node):
        if not node:
            return node

        def clone(node, nodes):
            if not node:
                return None
            if node.val in nodes:
                return nodes[node.val]
            cloned = Node(node.val, [])
            nodes[cloned.val] = cloned
            for x in node.neighbors:
                new_x = clone(x, nodes)
                cloned.neighbors.append(new_x)
            return cloned

        return clone(node, {})
