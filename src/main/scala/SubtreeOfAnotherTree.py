class Solution:
    def isSubtree(self, s, t):

        def find_subtree(root, node):
            if not root:
                return False
            return root.val == node.val and is_subtree(root, node) or find_subtree(root.left, node) or find_subtree(
                root.right, node)

        def is_subtree(root, node):
            if not root and not node:
                return True
            if not root or not node or root.val != node.val:
                return False
            return is_subtree(root.left, node.left) and is_subtree(root.right, node.right)

        return find_subtree(s, t)
