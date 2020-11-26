from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        if not root or root.left is None and root.right is None:
            return False

        def find(node, x):
            if not node:
                return None
            if node.val == x:
                return node
            l = find(node.left, x)
            if l:
                return l
            return find(node.right, x)

        def count(node):
            if not node:
                return 0
            left = count(node.left)
            right = count(node.right)
            return left + right + 1

        node = find(root, x)
        # count x nodes
        c1 = count(node)
        #count upper subtree
        p = n - c1
        #count left subtree
        l = count(node.left)
        #count right subtree
        r = count(node.right)
        return p > l + r + 1 or l > p + r + 1 or r > p + l + 1

