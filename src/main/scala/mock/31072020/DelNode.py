# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def delNodes(self, root: TreeNode, to_delete):
        if not root:
            return []
        deleted = set(to_delete)

        forest = []

        def traverse(node, deleted, forest):
            if not node:
                return
            if node.val not in deleted:
                forest[-1].append(node.val)
                traverse(node.left, deleted, forest)
                traverse(node.right, deleted, forest)
            else:
                if node.left:
                    forest.append([])
                    traverse(node.left, deleted, forest)
                if node.right:
                    forest.append([])
                    traverse(node.right, deleted, forest)

        traverse(root, deleted, forest)
        return forest


