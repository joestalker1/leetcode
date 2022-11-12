# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root, targetSum):
        if not root:
            return []

        def visit(node, cur_sum, cur_path, path_list):
            if not node:
                return
            cur_path.append(node.val)
            if not node.left and not node.right and cur_sum + node.val == targetSum:
                path_list.append(cur_path[::])
            else:
                visit(node.left, cur_sum + node.val, cur_path, path_list)
                visit(node.right, cur_sum + node.val, cur_path, path_list)
            cur_path.pop()

        path_list = []
        visit(root, 0, [], path_list)
        return path_list