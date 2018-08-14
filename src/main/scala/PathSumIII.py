class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def find_path(self, root, target, sum):
        if not root:
            return 0
        sum += root.val
        count = 0
        if sum == target:
            count += 1
        return count + self.find_path(root.left, target, sum) + self.find_path(root.right, target, sum)

    def pathSum(self, root, sum):
        if not root:
            return 0
        queue = [root]
        num = 0
        while len(queue) > 0:
            node = queue.pop()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            num += self.find_path(node, sum, 0)
        return num

sol = Solution()
root = TreeNode(1)
root.left = TreeNode(-2)
root.right = TreeNode(-3)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.left.left.left = TreeNode(-1)
root.right.left = TreeNode(-2)
print(sol.pathSum(root, -1))


root = TreeNode(-1)
root.right = TreeNode(-2)
root.right.right = TreeNode(-3)
root.right.right.right = TreeNode(4)
root.right.right.right.right = TreeNode(-3)
print(sol.pathSum(root, -3))


