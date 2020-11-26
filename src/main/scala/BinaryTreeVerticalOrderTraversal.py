class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


from collections import defaultdict

class Solution:
    def verticalOrder(self, root):

        if not root:
            return []
        m = defaultdict(list)
        q = [[root,0]]
        while len(q) > 0:
            node,col = q.pop()
            m[col].append(node.val)
            if node.left:
                q.append([node.left, col - 1])
            if node.right:
                q.append([node.right, col + 1])
        res = []
        for col in sorted(m.keys()):
            res.extend(m[col])
        return res
