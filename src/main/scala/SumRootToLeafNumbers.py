class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNumbers(self, root):
        def traverse(node, root_num):
            if not node:
                return 0
            new_root_num = root_num * 10 + node.val
            if not node.right and not node.left:
                return new_root_num
            return traverse(node.left, new_root_num) + traverse(node.right, new_root_num)

        return traverse(root, 0)

node = TreeNode(4)
node.right = TreeNode(0)
node.left = TreeNode(9)
node.left.left = TreeNode(5)
node.left.right = TreeNode(1)
sol = Solution()
print(sol.sumNumbers(node))
