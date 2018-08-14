# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import sys

class Solution:
    def nearVal(self, root, x):
        if root is None:
            return sys.maxsize
        else:
            min1 = abs(x - root.val)
            near1 = self.nearVal(root.left, x)
            min2 = abs(near1 - x)
            near2 = self.nearVal(root.right, x)
            min3 = abs(near2 - x)
            if min1 < min2:
                if min1 < min3:
                    return root.val
                return near2
            elif min1 > min2:
                if min2 < min3:
                    return near1
                return near2
            elif min3 < min2:
                if min3 < min1:
                    return near2
                return root.val

    def minDiffInBST(self, root):
        if root is None:
            return sys.maxsize
        near1 = self.nearVal(root.left, root.val)
        near2 = self.nearVal(root.right, root.val)
        min1 = min(abs(root.val - near1), abs(root.val - near2))
        min2 = self.minDiffInBST(root.left)
        min3 = self.minDiffInBST(root.right)
        return min(min1, min2, min3)


root = TreeNode(90)
n1 = TreeNode(69)
root.left = n1
n1.right = TreeNode(89)
n1.left = TreeNode(49)
n1.left.right = TreeNode(52)
sol = Solution()
print(sol.minDiffInBST(root))

