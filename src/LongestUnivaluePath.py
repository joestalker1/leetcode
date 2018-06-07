class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def longestUnivaluePath(self, root):
        self.ans = 0


        def path_len(node):
            if not node:
                return 0
            left_len = path_len(node.left)
            right_len = path_len(node.right)
            left_arrow = right_arrow = 0
            if node.left and node.left.val == node.val:
                left_arrow = left_len + 1
            if node.right and node.right.val == node.val:
                right_arrow = right_len + 1
            self.ans = max(self.ans, left_arrow + right_arrow)
            return max(left_arrow, right_arrow)
        path_len(root)
        return self.ans


sol = Solution()
root = TreeNode(26)
root.left = TreeNode(26)
root.left.left = TreeNode(26)
root.right = TreeNode(26)
root.right.left = TreeNode(26)
root.right.right = TreeNode(26)
print(sol.longestUnivaluePath(root))

root = TreeNode(1)
root.left = TreeNode(2)
print(sol.longestUnivaluePath(root))

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(1)
root.right.right = TreeNode(5)
print(sol.longestUnivaluePath(root))

root = TreeNode(1)
root.left = TreeNode(1)
root.right = TreeNode(1)
print(sol.longestUnivaluePath(root))

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(1)
print(sol.longestUnivaluePath(root))
