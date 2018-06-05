class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def cons_or_snoc(self, queue, node, cur_value):
        if not node:
            return
        if node.val == cur_value:
            queue.insert(0, node)
        else:
            queue.append(node)

    def longestUnivaluePath(self, root):
        if not root:
            return 0
        queue = []
        queue.append(root)
        max_len = 1
        cur_len = 1
        cur_value = -1
        while len(queue) > 0:
            node = queue.pop(0)

            if cur_value == node.val:
                cur_len += 1
            else:
                if cur_len > max_len:
                    max_len = cur_len
                cur_value = node.val
                cur_len = 1


            if node.left and node.right and node.left.val == node.right.val:
                queue.insert(0, node.right)
                queue.insert(0, node.left)
            else:
                self.cons_or_snoc(queue, node.left, cur_value)
                self.cons_or_snoc(queue, node.right, cur_value)


        return (max_len - 1) if cur_len < max_len else (cur_len - 1)


sol = Solution()
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(1)
root.right.right = TreeNode(5)
print(sol.longestUnivaluePath(root))

root= TreeNode(1)
root.left = TreeNode(1)
root.right = TreeNode(1)
print(sol.longestUnivaluePath(root))

root= TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(1)
print(sol.longestUnivaluePath(root))