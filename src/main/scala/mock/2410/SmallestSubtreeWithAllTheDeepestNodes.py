# Definition for a binary tree node.
from utils import TreeNode,arrayToTreeNode

class Solution:
    def subtreeWithAllDeepest(self, root):
        if not root:
            return []

        def depth(node):
            if not node:
                return 0
            left_depth = 1 + depth(node.left)
            right_depth = 1 + depth(node.right)
            return max(left_depth, right_depth)

        def is_leaf(node):
            return node and node.right is None and node.left is None

        def sub_tree(node, d):
            if d == 0:
                return node
            if not node:
                return None
            left_tree = sub_tree(node.left, d - 1)
            right_tree = sub_tree(node.right, d - 1)
            if left_tree and right_tree:
                return node
            if left_tree:
                return left_tree
            return right_tree

        if is_leaf(root):
            return root

        d = depth(root) - 1 # number of nodes
        return sub_tree(root, d)


sol = Solution()
arr = [0,1,3, None,2]
tree = arrayToTreeNode(arr)
print(sol.subtreeWithAllDeepest(tree))
arr = [3,5,1,6,2,0,8, None, None,7,4]
tree = arrayToTreeNode(arr)
sol = Solution()
print(sol.subtreeWithAllDeepest(tree))
