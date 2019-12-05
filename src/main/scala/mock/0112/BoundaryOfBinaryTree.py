from utils import TreeNode,arrayToTreeNode

class Solution(object):
    def boundaryOfBinaryTree(self, root):
        if not root:
            return []

        def left_boundary(node, seen, res):
            if not node:
                return
            if node not in seen:
                res.append(node.val)
                seen.add(node)
            left_boundary(node.left, seen, res)
            if not node.left:
                left_boundary(node.right, seen, res)

        def right_boundary(node, seen, res):
            if not node:
                return
            if node not in seen:
                res.append(node.val)
                seen.add(node)
            right_boundary(node.right, seen, res)
            if not node.right:
                #probably it will be included to leaf
                right_boundary(node.left, seen, res)

        def leaves(node, seen, res):
            if not node:
                return
            leaves(node.left, seen, res)
            if not node.left and not node.right and node not in seen:
                res.append(node.val)
                seen.add(node)
            leaves(node.right, seen, res)
        seen = set()
        lefts = []
        leave_list = []
        rights = []
        left_boundary(root.left, seen, lefts)
        leaves(root, seen, leave_list)
        right_boundary(root.right, seen, rights)
        rights.reverse()
        return [root.val] + lefts +  leave_list + rights


sol = Solution()
arr = [1,2,3,4,5,6, None, None, None,7,8,9,10]#[1,2,4,7,8,9,10,6,3]
root = arrayToTreeNode(arr)
print(sol.boundaryOfBinaryTree(root))

arr = [4,2, None,3,1, None, None,5]#[4,2,3,5]
root = arrayToTreeNode(arr)
print(sol.boundaryOfBinaryTree(root))











