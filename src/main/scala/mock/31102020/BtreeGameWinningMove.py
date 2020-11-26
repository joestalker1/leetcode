# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import defaultdict


class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        if not root or root.left is None and root.right is None:
            return False

        node_map = defaultdict(int)
        level_node = defaultdict(list)

        def fill_node_map(node, level):
            if not node:
                return [0, 0]
            node_map[node.val] = [1, level]
            level_node[level].append(node.val)
            left = fill_node_map(node.left, level + 1)
            right = fill_node_map(node.right, level + 1)
            node_map[node.val][0] += (left[0] + right[0])
            return node_map[node.val]

        def count(node, x):
            if not node or node.val == x:
                return 0
            left = count(node.left, x)
            right = count(node.right, x)
            return left + right + 1

        fill_node_map(root, 0)
        n1, l1 = node_map[x]
        n2 = count(root, x)
        return n2 > n1





