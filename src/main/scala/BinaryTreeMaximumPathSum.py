class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.max_sum = -inf

        def find_max_sum(node):
            if not node:
                return 0
            left_sum = max(0, find_max_sum(node.left))
            right_sum = max(0, find_max_sum(node.right))
            self.max_sum = max(self.max_sum, node.val + left_sum + right_sum)
            return max(left_sum, right_sum) + node.val

        find_max_sum(root)
        return self.max_sum