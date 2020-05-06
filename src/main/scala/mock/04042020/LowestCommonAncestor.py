# Definition for a binary tree node.
import utils
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or not p or not q:
            return None
        parent = {}

        def find_parent(node, par):
            if not node:
                return
            parent[node] = par
            find_parent(node.left, node)
            find_parent(node.right, node)

        find_parent(root, root)
        ancestors = set()
        v = p
        ancestors.add(v)
        while v in parent and parent[v] != v:
            ancestors.add(v)
            v = parent[v]
        ancestors.add(root)
        v = q
        while v in parent and parent[v] != v:
            if v in ancestors:
                return v
            v = parent[v]
        return root

root = [3,5,1,6,2,0,8,None,None,7,4]
tree = utils.arrayToTreeNode(root)
sol = Solution()
print(sol.lowestCommonAncestor(tree, 5,4))







