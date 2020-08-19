class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        high = 0
        node = root
        while node.left:
            high += 1
            node = node.left
        N = 2 ** (h + 1) - 1

        def countLeaves(node, high, level):
            if not node:
                return 0
            left_count = countLeaves(node.left, high, level + 1)
            if not node.left and not node.right and high == level:
                left_count += 1
            right_count = countLeaves(node.right, high, level + 1)
            return left_count + right_count

        leaves = countLeaves(root, high, 0)
        return N - leaves
