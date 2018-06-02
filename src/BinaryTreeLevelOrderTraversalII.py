class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Solution:
    def add_or_create(self, res, level, a):
        if len(res) <= level:
            for i in range(level + 1 - len(res)):
                res.append([])
        res[level].append(a)

    def level_order_bottom(self, root, level, res):
        if not root:
            return
        self.level_order_bottom(root.left,level + 1, res)
        self.level_order_bottom(root.right,level + 1, res)
        self.add_or_create(res, level, root.val)

    def levelOrderBottom(self, root):
        res = []
        self.level_order_bottom(root, 0, res)
        if res:
           res = list(reversed(res))
        return res

sol = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.right = TreeNode(5)
print(sol.levelOrderBottom(root))

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(sol.levelOrderBottom(root))



