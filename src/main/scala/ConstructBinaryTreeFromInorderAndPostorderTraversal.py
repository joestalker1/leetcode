# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder:
            return None
        in_ixd = {x: i for i,x in enumerate(inorder)}
        post_idx = len(inorder) - 1

        def build(in_idx, in_s = 0, in_e = len(inorder)):
            nonlocal post_idx
            if in_s == in_e:
                return None
            x = postorder[post_idx]
            root = TreeNode(x)
            post_idx -= 1
            index = in_idx[x]
            root.right = build(in_idx, index + 1, in_e)
            root.left = build(in_idx, in_s, index)
            return root

        return build(in_ixd)

sol = Solution()
sol.buildTree([9,3,15,20,7], [9,15,7,20,3])