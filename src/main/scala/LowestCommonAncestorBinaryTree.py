# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def find_node(self, root, x, nodes):
        if not root:
            return None
        if root.val == x.val:
            nodes.append(root)
            return root
        res = self.find_node(root.left, x, nodes)
        if res:
            nodes.append(root)
            return res
        res = self.find_node(root.right, x, nodes)
        if res:
            nodes.append(root)
        return res

    def find_first_equal(self, l1, l2):
        nodes = set(l1)
        for j in range(len(l2)):
            if l2[j] in nodes:
                return l2[j]
        return None

    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return None
        if root.val == p.val or root.val == q.val:
            return root
        nodes1 = []
        resp1 = self.find_node(root.left, p, nodes1)
        resp2 = None
        if not resp1:
            resp2 = self.find_node(root.right, p, nodes1)
        nodes2 = []
        resq1 = self.find_node(root.left, q, nodes2)
        resq2 = None
        if not resq1:
            resq2 = self.find_node(root.right, q, nodes2)
        if resp1 and resq1 or resp2 and resq2: # both left
            return self.find_first_equal(nodes1, nodes2)
        if resp1 and resq2 or resp2 and resq1:
            return root


sol = Solution()
root = TreeNode(-1)
root.left = TreeNode(0)
root.right = TreeNode(3)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.left.left = TreeNode(8)
print(sol.lowestCommonAncestor(root, TreeNode(8), TreeNode(4)))