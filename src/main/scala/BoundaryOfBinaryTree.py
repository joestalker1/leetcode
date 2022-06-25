# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def boundaryOfBinaryTree(self, root):
        if not root:
            return []

        def is_leaf(node):
            return not node.right and not node.left

        def leaves(node, nodes):
            if not node:
                return
            if is_leaf(node):
                nodes.append(node.val)
            leaves(node.left, nodes)
            leaves(node.right, nodes)
        res = []
        if not is_leaf(root):
            res.append(root.val)
        t = root.left
        while t:
            if not is_leaf(t):
                res.append(t.val)
            if t.left:
                t = t.left
            else:
                t = t.right
        leaves(root, res)
        st = []
        t = root.right
        while t:
            if not is_leaf(t):
                st.append(t.val)
            if t.right:
                t = t.right
            else:
                t = t.left
        while st:
            a = st.pop()
            res.append(a)
        return res





