class Solution:
    def increasingBST(self, root):
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            node.left = None
            # self.cur points the lesser node
            self.cur.right = node
            self.cur = node
            inorder(node.right)

        new_root = self.cur = TreeNode(0)
        inorder(root)
        return new_root.right

