# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def increasingBST(self, root):
        if not root:
            return root

        def rearrange(node):
            if not node:
                return None
            if not node.left and not node.right:
                return TreeNode(node.val)
            left_subtree = rearrange(node.left)
            #left_subtree is new root
            #find the rightmost node
            rightmost_leave = left_subtree
            while rightmost_leave and rightmost_leave.right:
                rightmost_leave = rightmost_leave.right
            new_node = TreeNode(node.val)
            if rightmost_leave:
                rightmost_leave.right = new_node
            new_node.right = rearrange(node.right)
            return left_subtree if left_subtree else new_node

        return rearrange(root)
