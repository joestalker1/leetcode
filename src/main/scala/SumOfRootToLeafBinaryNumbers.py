# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root) -> int:
        leafes_sum = 0

        def calc_sum(node, num):
            nonlocal leafes_sum
            if not node:
                return
            new_num = (num << 1) + node.val
            if not node.left and not node.right:
                leafes_sum += new_num
            calc_sum(node.left, new_num)
            calc_sum(node.right, new_num)

        calc_sum(root, 0)
        return leafes_sum
