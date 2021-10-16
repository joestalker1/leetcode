class ListNode:
    def __init__(self, v):
        self.val = v
        self.left = None
        self.right = None
        self.nextRight = None


class Solution:
    def connect(self, root):

        def getNextNode(node):
            t = node.nextRight
            while t:
                if t.left:
                    return t.left
                if t.right:
                    return t.right
                t = t.nextRight
            return None

        def connect(node):
            if not node:
                return
            if node.nextRight:
                connect(node.nextRight)
            if node.left:
                if node.right:
                    node.left.nextRight = node.right
                    node.right = getNextNode(node)
                else:
                    node.left = getNextNode(node)
                connect(node.left)
            elif node.right:
                node.right.nextRight = getNextNode(node)
                connect(node.right)
            else:
                connect(getNextNode(node))
        connect(root)

sol = Solution()
root = ListNode(1)
root.left = ListNode(2)
root.left.left = ListNode(4)
root.left.right = ListNode(5)
root.right = ListNode(3)
root.right.right = ListNode(6)
sol.connect(root)
