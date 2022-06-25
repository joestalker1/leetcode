# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root):
        def build_tree(node, right_subtree_sum):
            if not node:
                return 0
            # go to the right subtree
            right_sum = build_tree(node.right, right_subtree_sum)
            prev = node.val
            # update curret node
            node.val += right_sum + right_subtree_sum
            # go to the left subtree
            left_sum = build_tree(node.left, node.val)
            # return left,right subtrees and node.val
            return left_sum + right_sum + prev

        build_tree(root, 0)
        return root
