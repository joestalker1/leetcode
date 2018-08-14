
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        def traverse(node, level,res):
            if not node:
                return
            if len(res) <= level:
                res.append([])
            res[level].append(node.val)
            traverse(node.left, level + 1, res)
            traverse(node.right, level + 1, res)
        res = []
        traverse(root, 0, res)
        return res
