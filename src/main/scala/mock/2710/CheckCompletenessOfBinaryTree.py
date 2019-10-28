from utils import TreeNode,arrayToTreeNode

class Solution(object):
    def isCompleteTree(self, root):
        if not root:
            return False
        nodes = [root]
        while nodes[0] is not None:
            node = nodes.pop(0)
            nodes.append(node.left)
            nodes.append(node.right)
        while len(nodes) > 0 and nodes[0] is None:
            nodes.pop(0)
        return len(nodes) == 0

sol = Solution()
arr = [1,2,3, None, None,7,8]
tree = arrayToTreeNode(arr)
#print(sol.isCompleteTree(tree))#false
arr = [1,2,3,4,5,6]
tree = arrayToTreeNode(arr)
print(sol.isCompleteTree(tree))#true
arr = [1,2,3,4,5, None, 7]
tree = arrayToTreeNode(arr)
print(sol.isCompleteTree(tree))#false





