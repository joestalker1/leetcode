# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        if not root:
            return 0
        diameter = 0

        def get_height(node):
            nonlocal diameter
            if not node:
                return 0
            left_height = get_height(node.left)
            right_height = get_height(node.right)
            # count path that going through node
            diameter = max(diameter, left_height + right_height)
            # plus 1 we count edge between node's parent and node
            return 1 + max(left_height, right_height)

        get_height(root)
        return diameter

