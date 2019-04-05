class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import defaultdict

class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
        if not root:
            return []

        def traverse(node, level, m):
            if not node:
                return
            if level % 2 == 0:
                m[level].append(node.val)
            else:
                m[level].insert(0, node.val)
            traverse(node.left, level + 1, m)
            traverse(node.right, level + 1, m)

        m = defaultdict(list)
        traverse(root, 0, m)
        j = 0
        res = []
        while True:
            if j not in m:
                break
            res.append(m[j])
            j += 1
        return res

r = TreeNode(1)
r.left = TreeNode(2)
r.right = TreeNode(3)
r.left.left = TreeNode(4)
r.right.right = TreeNode(5)

sol = Solution()
print(sol.zigzagLevelOrder(r))
#[1,2,3,4,null,null,5]



