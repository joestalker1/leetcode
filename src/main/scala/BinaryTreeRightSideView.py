# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def rightSideView(self, root):
        if not root:
            return []
        max_depth = 0

        def traverse(node, level, level_to_val):
            nonlocal max_depth
            if not node:
                return
            traverse(node.right, level + 1, level_to_val)
            traverse(node.left, level + 1, level_to_val)
            if level not in level_to_val:
                level_to_val[level] = node.val
            max_depth = max(level, max_depth)


        level_to_val = {}
        traverse(root, 0, level_to_val)
        return [level_to_val[depth] for depth in range(max_depth + 1)]


sol = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
root.right.right = TreeNode(4)

print(sol.rightSideView(root))

