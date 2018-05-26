class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def add_childer(self, list):
        nodes = []
        for node in list:
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
        return nodes

    def averageOfLevels(self, root):
        nodes = []
        res = []
        nodes.append(root)
        while len(nodes) > 0:
            avg = sum(a.val for a in nodes)
            avg /= len(nodes)
            res.append(avg)
            nodes = self.add_childer(nodes)
        return res

sol = Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(sol.averageOfLevels(root))


