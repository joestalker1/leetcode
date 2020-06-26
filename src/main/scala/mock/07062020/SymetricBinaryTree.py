class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import utils

class Solution:
    def isSymmetric(self, root):
        if not root:
            return True

        def traverse(left_tree, right_tree):
            if not left_tree and not right_tree:
                return True
            if not left_tree and right_tree:
                return False
            if left_tree and not right_tree:
                return False
            if left_tree.val != right_tree.val:
                return False

            return traverse(left_tree.left, right_tree.right) and traverse(left_tree.right, right_tree.left)

        return traverse(root.left, root.right)


sol = Solution()
arr = [1,2,2,3,4,4,3]
root = utils.arrayToTreeNode(arr)
print(sol.isSymmetric(root))