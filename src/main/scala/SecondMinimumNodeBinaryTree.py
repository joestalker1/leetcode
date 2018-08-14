class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def findSecondMinimumValue(self, root):
        if not root:
            return -1
        min1 = root.val
        self.ans = float("inf")
        def dfs(node):
            if node:
                if min1 < node.val < self.ans:
                    self.ans = node.val
                elif node.val == min1:
                    dfs(node.left)
                    dfs(node.right)
        dfs(root)
        return self.ans if self.ans < float("inf") else -1

sol = Solution()
root = TreeNode(2)
#root.left = TreeNode(2)
#root.right = TreeNode(2)
print(sol.findSecondMinimumValue(root))
