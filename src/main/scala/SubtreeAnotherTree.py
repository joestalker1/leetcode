class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None




class Solution:
    def compare(self, root, sub_tree):
        if not root and not sub_tree:
            return True
        if not root or not sub_tree or root.val != sub_tree.val:
            return False
        return self.compare(root.left,sub_tree.left) and self.compare(root.right, sub_tree.right)

    def isSubtree(self, root, sub_tree):
        if not root and not sub_tree:
            return True
        if not root or not sub_tree or root.val != sub_tree.val:
            return False
        if self.compare(root, sub_tree):
            return True
        return self.compare(root.left, sub_tree.left) or self.compare(root.right, sub_tree.right)

sol = Solution()
root = TreeNode(1)
root.left = TreeNode(1)
print(sol.isSubtree(root, TreeNode(1)))