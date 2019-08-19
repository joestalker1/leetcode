# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        in_idx = {x: i for i, x in enumerate(inorder)}

        def build(in_idx, in_s, in_e):
            nonlocal pre_idx
            if in_s == in_e:
                return None
            x = preorder[pre_idx]
            root = TreeNode(x)
            index = in_idx[x]
            pre_idx += 1
            root.left = build(in_idx, in_s, index)
            root.right = build(in_idx, index + 1, in_e)
            return root

        pre_idx = 0
        root = build(in_idx, 0, len(inorder))
        return root


sol = Solution()
print(sol.buildTree([3,9,20,15,7], [9,3,15,20,7]))

