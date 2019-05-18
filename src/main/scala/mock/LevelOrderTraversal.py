# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import defaultdict


class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        m = defaultdict(list)

        def traverse(node, level, m):
            if not node:
                return
            m[level].append(node.val)
            traverse(node.left, level + 1, m)
            traverse(node.right, level + 1, m)

        traverse(root, 0, m)
        i = 0
        res = []
        while i in m.keys():
            res.append(m[i])
            i += 1
        return res

sol = Solution()
print(sol.levelOrder(None))
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(sol.levelOrder(root))