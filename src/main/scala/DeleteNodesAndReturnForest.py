class Solution:
    def delNodes(self, root: TreeNode, to_delete):
        if not root:
            return None

        forest = []
        to_del = set(to_delete)

        def traverse(node, to_del, forest):
            if not node:
                return
            # call it for left,right subtrees
            node.left = traverse(node.left, to_del, forest)
            node.right = traverse(node.right, to_del, forest)

            # if node is in to_delete
            if node.val in to_del:
                # check if it's not empty node
                if node.left:
                    forest.append(node.left)
                if node.right:
                    forest.append(node.right)
                return None
            return node

        traverse(root, to_del, forest)

        if root.val not in to_del:
            forest.append(root)

        return forest
