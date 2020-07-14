from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root):
        if not root:
            return []

        q = [[0, root]]
        m = defaultdict(list)
        while q:
            level, node = q.pop(0)
            m[level].append(node.val)
            if node.left:
                q.append([level + 1, node.left])
            if node.right:
                q.append([level + 1, node.right])
        res = []
        for level in range(max(m.keys()) + 1):
            avg = sum(m[level]) / len(m[level])
            res.append(avg)
        return res


