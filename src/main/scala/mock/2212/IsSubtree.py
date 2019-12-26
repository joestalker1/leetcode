# Definition for a binary tree node.
from utils import arrayToTreeNode


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubtree(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False

        def find_root(node, subnode):
            if not node:
                return False
            if node.val == subnode.val:
                if is_subtree(node, subnode):
                    return True
            if find_root(node.left, subnode):
                return True
            return find_root(node.right, subnode)

        def is_subtree(node, subnode):
            if not node and not subnode:
                return True
            if not node or not subnode:
                return False
            if node.val != subnode.val:
                return False
            left_tree = is_subtree(node.left, subnode.left)
            if not left_tree:
                return False
            return is_subtree(node.right, subnode.right)

        return find_root(s, t)



sol = Solution()
s = arrayToTreeNode([1, 1])
t = arrayToTreeNode([1])
print(sol.isSubtree(s, t))

s = arrayToTreeNode([3, 4, 5, 1, 2])
t = arrayToTreeNode([4, 1, 2])
print(sol.isSubtree(s, t))
