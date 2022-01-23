class Solution:
    def buildTree(self, inorder, postorder):
        # index of postorder
        last = len(postorder) - 1

        def traverse(pos_to_node, l, r):
            nonlocal last
            if l > r:
                return None
            val = postorder[last]
            last -= 1
            node = TreeNode(val)
            p = pos_to_node[val]
            node.right = traverse(pos_to_node, p + 1, r)
            node.left = traverse(pos_to_node, l, p - 1)
            return node

        pos_to_node = {inorder[i]: i for i in range(len(postorder))}

        return traverse(pos_to_node, 0, len(inorder) - 1)
