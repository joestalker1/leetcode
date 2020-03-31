class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def left_boundary(self, root, nodes):
        if not root:
            return
        if root.left:
            self.left_boundary(root.left, nodes)
        else:
            self.left_boundary(root.right, nodes)
        nodes.append(root.val)

    def leaves(self, root, nodes):
        if not root:
            return
        self.leaves(root.left, nodes)
        if not root.right and not root.left:
            nodes.append(root.val)
        self.leaves(root.right, nodes)

    def right_boundary(self, root, nodes):
        if not root:
            return
        if root.right:
            self.right_boundary(root.right, nodes)
        else:
            self.left_boundary(root.left, nodes)
        nodes.append(root.val)


    def boundaryOfBinaryTree(self, root):
        if not root:
            return []
        left_nodes = []
        self.left_boundary(root.left, left_nodes)
        leaves_nodes = []
        self.leaves(root.left, leaves_nodes)
        self.leaves(root.right, leaves_nodes)
        right_nodes = []
        self.right_boundary(root.right,right_nodes)
        left_nodes.reverse()
        res = [root.val] + left_nodes
        seen = set(res)
        for n in leaves_nodes:
            if res[-1] != n and n not in seen:
                res.append(n)
                seen.add(n)
        for n in right_nodes:
            if res[-1] != n and n not in seen:
                res.append(n)
        return res

sol = Solution()
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
root.right.right = TreeNode(4)
print(sol.boundaryOfBinaryTree(root))

#[37,-34,-48,null,-100,-100,48,null,null,null,null,-54,null,-71,-22,null,null,null,8]