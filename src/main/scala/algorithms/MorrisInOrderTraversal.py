# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root):
        if not root:
            return []
        res = []
        cur = root
        pre = None
        while cur:
            if not cur.left:
                res.append(cur.val)
                cur = cur.right
            else:
                pre = cur.left
                while pre.right:
                    pre = pre.right
                pre.right = cur
                temp = cur
                cur = cur.left
                temp.left = None
        return res