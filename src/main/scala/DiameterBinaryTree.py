class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def __init__(self):
        self.max_diameter = 1

    def max_path(self, root):
        if not root:
            return 0
        left_path = self.max_path(root.left)
        right_path = self.max_path(root.right)
        new_diameter = 1 + left_path + right_path
        self.max_diameter = max(new_diameter, self.max_diameter)
        return 1 + max(left_path, right_path)


    def diameterOfBinaryTree(self, root):
        self.max_path(root)
        return self.max_diameter - 1
