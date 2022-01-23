class Solution(object):
    def treeToDoublyList(self, root):
        if not root:
            return root
        first = None
        last = None

        def convert(node):
            nonlocal first, last
            if not node:
                return node
            convert(node.left)
            if last:
                last.right = node
                node.left = last
            else:
                first = node
            last = node
            convert(node.right)

        convert(root)
        first.left = last
        last.right = first
        return first
