class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        q = [[root, 0]]
        res = []
        while q:
            node, level = q.pop(0)
            if len(res) < level + 1:
                res.append([])

            if level % 2 == 0:  # left to right
                res[level].insert(0, node.val)
            else:
                res[level].append(node.val)

            if node.left:
                q.append([node.left, level + 1])
            if node.right:
                q.append([node.right, level + 1])
        return res        
