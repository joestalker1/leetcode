# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math


class Solution:
    def longestConsecutive(self, root) -> int:
        if not root:
            return 0

        def dfs(node, cur_len, prev_val):
            if not node:
                return cur_len
            if prev_val + 1 == node.val:
                cur_len += 1
            else:
                cur_len = 1
            left_len = dfs(node.left, cur_len, node.val)
            right_len = dfs(node.right, cur_len, node.val)
            return max(cur_len, left_len, right_len)

        return dfs(root, 0, -math.inf)