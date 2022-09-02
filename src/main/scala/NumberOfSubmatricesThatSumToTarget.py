from math import inf

class Solution:
    def maxSumBST(self, root) -> int:
        if not root:
            return 0
        # min,max,sum
        max_sum = 0

        def traverse_bst(node):
            nonlocal max_sum
            if not node:
                return (inf, -inf, 0)
            left = traverse_bst(node.left)
            right = traverse_bst(node.right)
            if not (left and right and node.val > left[1] and node.val < right[0]):
                return None
            cur_sum = left[2] + right[2] + node.val
            max_sum = max(max_sum, cur_sum)
            return (min(node.val, left[0]), max(node.val, right[1]), cur_sum)

        traverse_bst(root)
        return max_sum