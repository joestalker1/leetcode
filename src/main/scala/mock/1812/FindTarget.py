# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findTarget(self, root, k):
        if not root:
            return False

        m = set()
        q = [root]
        while q:
            node = q.pop(0)
            rem = k - node.val
            if rem in m:
                return True
            m.add(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return False