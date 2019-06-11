class Node(object):
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def treeToDoublyList(self, root):
        def traverse(node):
            nonlocal first, last
            if node:
                traverse(node.left)
                if last:
                    node.left = last
                    last.right = node.left
                else:
                    first = node
                last = node
                traverse(node.right)
        first, last = None, None
        traverse(root)
        last.right = first
        first.left = last
        return first


root = Node(4)
root.left = Node(2)
root.left.left = Node(1)
root.left.right = Node(3)
root.right = Node(5)
root.right.right = Node(6)
sol = Solution()
head = sol.treeToDoublyList(root)
print(head)
