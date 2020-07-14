class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder, postorder):
        if not inorder and not postorder:
            return None
        node_pos = {x: i for i, x in enumerate(inorder)}
        last_node = len(postorder) - 1

        def traverse(node_pos, s, e):
            nonlocal last_node
            if s > e:
                return None
            x = postorder[last_node]
            last_node -= 1
            new_s = node_pos[x]
            node = TreeNode(x)
            node.right = traverse(node_pos, new_s + 1, e)
            node.left = traverse(node_pos, s, new_s - 1)
            return node

        return traverse(node_pos, 0, len(inorder) - 1)


sol = Solution()
root = sol.buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3])
