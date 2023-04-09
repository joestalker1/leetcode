class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        max_diff = 0

        def find_max_diff(node, min_val, max_val):
            nonlocal max_diff
            if not node:
                return
            max_diff = max(max_diff, abs(node.val - min_val), abs(node.val - max_val))
            min_val = min(min_val, node.val)
            max_val = max(max_val, node.val)
            find_max_diff(node.left, min_val,max_val)
            find_max_diff(node.right,min_val, max_val)

        find_max_diff(root, root.val, root.val)
        return max_diff
