# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEqualTree(self, root) -> bool:
        if not root:
            return False

        sums = []

        def sum_tree(node, sums):
            if not node:
                return 0
            sums.append(node.val + sum_tree(node.left, sums) + sum_tree(node.right, sums))
            return sums[-1]

        total = sum_tree(root, sums)
        # remove root + left substre + right subtree
        sums.pop()
        return total % 2 == 0 and total // 2 in sums