class Solution:
    def flatten(self, root) -> None:
        if not root:
            return None

        def flat_list(node):
            if not node:
                return None
            if not node.left and not node.right:
                return node
            left_tail = flat_list(node.left)
            right_tail = flat_list(node.right)
            if left_tail:
                left_tail.right = node.right
                node.right = node.left
                node.left = None
            return right_tail if right_tail else left_tail

        flat_list(root)
        return root