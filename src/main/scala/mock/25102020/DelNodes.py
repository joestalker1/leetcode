class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def delNodes(self, root: TreeNode, to_delete):
        if not root:
            return []

        def dfs(node, res):
            if not node:
                return
            if node.val in to_delete:
                if node.left:
                    res.append(node.left.val)
                if node.right:
                    res.append(node.right.val)
            dfs(node.left, res)
            dfs(node.right, res)

        res = []
        if res.val not in to_delete:
            res.append(root.val)
        dfs(root, res)
        return res



