# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import defaultdict

class Solution:
    def largestValues(self, root: TreeNode):
        if not root:
            return []
        res = defaultdict(int)
        q = [[root, 0]]
        while q:
            n,level = q.pop(0)
            res[level] = max(res[level], n.val)
            if n.left:
                q.append([n.left,level + 1])
            if n.right:
                q.append([n.right, level + 1])
        return [v for k,v in res.items()]