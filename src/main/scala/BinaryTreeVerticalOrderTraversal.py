class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def verticalOrder(self, root):
        if not root:
            return []
        map = {}
        q = []
        cols = []
        q.append(root)
        cols.append(0)
        min_col = 0
        max_col = 0
        res = []
        while len(q) > 0:
            node = q.pop()
            col = cols.pop()
            if col not in map:
                map[col] = []
            map[col].append(node.val)
            if node.left:
                q.append(node.left)
                cols.append(col - 1)
                min_col = min(min_col, col-1)
            if node.right:
                q.append(node.right)
                cols.append(col + 1)
                max_col = max(max_col, col + 1)
        for i in range(min_col, max_col + 1):
            if i in map:
                res.append(map[i])
        return res
