class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def longestUnivaluePath(self, root):
        if not root:
            return 0
        nodes = [root]
        max_len = 0
        while len(nodes) > 0:
            same_nodes = [nodes.pop(0)]
            cur_len = 0
            while len(same_nodes) > 0:
                node = same_nodes.pop(0)
                cur_len += 1
                if node.left:
                    if node.left.val == node.val:
                        same_nodes.append(node.left)
                    else:
                        nodes.append(node.left)
                if node.right:
                    if node.right.val == node.val:
                        same_nodes.append(node.right)
                    else:
                        nodes.append(node.right)
            if cur_len > max_len:
                max_len = cur_len

        return max_len - 1

sol = Solution()
root = TreeNode(1)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(4)
root.left.right = TreeNode(4)
root.right.right = TreeNode(5)
print(sol.longestUnivaluePath(root))

