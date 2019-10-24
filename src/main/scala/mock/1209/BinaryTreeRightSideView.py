class Solution:
    def rightSideView(self, root):
        if not root:
            return []
        max_depth = 0
        rightmost_node = {}
        stack = [(root, 0)]
        while stack:
            node,depth = stack.pop()

            if node is not None:
                max_depth = max(max_depth, depth)
                if depth not in rightmost_node:
                    rightmost_node[depth] = node.val
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))
        return [rightmost_node[depth] for depth in range(max_depth + 1)]





