# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def closestValue(self, root: TreeNode, target: float):
        if not root:
            return float('inf')
        if target < root.val:
            left_val = self.closestValue(root.left, target)
            if abs(left_val - target) < abs(root.val - target):
                return left_val
        else:
            right_val = self.closestValue(root.right, target)
            if abs(right_val - target) < abs(root.val - target):
                return right_val
        return root.val

tree = TreeNode(2)
tree.left= TreeNode(0)
tree.right = TreeNode(3)

sol = Solution()
print(sol.closestValue(tree, 0.42857))



