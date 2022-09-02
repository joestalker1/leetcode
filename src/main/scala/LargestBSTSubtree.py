from math import inf


class Solution:
    def largestBSTSubtree(self, root) -> int:
        if not root:
            return 0

        max_cnt = 0

        def traverse(node):
            nonlocal max_cnt
            if not node:
                return (inf, -inf, 0)
            left = traverse(node.left)
            right = traverse(node.right)
            if not (left and right and left[1] < node.val and node.val < right[0]):
                return None
            cnt = left[2] + right[2] + 1
            max_cnt = max(cnt, max_cnt)
            return (min(node.val, left[0]), max(node.val, right[1]), cnt)

        traverse(root)
        return max_cnt
