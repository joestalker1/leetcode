from utils import TreeNode, arrayToTreeNode

class Solution:
    def __init__(self):
        self.min_str = None

    def to_char(self, code):
        return chr(ord('a') + code)

    def min_string(self, s1, s2):
        if not s1:
            return s2
        if not s2:
            return s1
        return min(s1, s2)

    def smallestFromLeaf(self, root):
        if not root:
            return root
        def traverse(node, str=''):
            if node and not node.left and not node.right:
                ch = self.to_char(node.val)
                s = ch + str[::-1]
                self.min_str = self.min_string(s, self.min_str)
                return
            if not node:
                return
            ch = self.to_char(node.val)
            traverse(node.left, str + ch)
            traverse(node.right, str + ch)
        self.min_str = None
        traverse(root)
        return self.min_str


sol = Solution()
arr = [25,1,None,0,0,1,None, None,None,0]
tree = arrayToTreeNode(arr)
print(sol.smallestFromLeaf(tree)) #"ababz"

arr = [4,0,1,1]
tree = arrayToTreeNode(arr)
print(sol.smallestFromLeaf(tree))

arr = [0, None, 1]
tree = arrayToTreeNode(arr)
print(sol.smallestFromLeaf(tree))

arr = [2,2,1,None,1,0,None,0]
tree = arrayToTreeNode(arr)
print(sol.smallestFromLeaf(tree))
