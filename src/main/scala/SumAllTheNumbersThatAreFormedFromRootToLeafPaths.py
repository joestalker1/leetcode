class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def getTreeSum(root):
    if not root:
        return 0

    def dfs(root, val):
        if not root:
            return 0
        val = val * 10 + root.data
        if not root.left and not root.right:
            return val
        return dfs(root.left, val) + dfs(root.right, val)

    return dfs(root, 0)


root = Node(6)
root.left = Node(5)
root.right = Node(7)
print(getTreeSum(root))