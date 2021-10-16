#User function Template for python3


'''
:param root: root of the given tree
:return: none, just connect accordingly.
{
    # Node Class:
    class Node:
        def __init__(self,val):
            self.data = val
            self.left = None
            self.right = None
            self.nextRight = None
}
'''

from collections import defaultdict

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
        self.nextRight = None


class Solution:
    def connect(self, root):
        if not root:
            return
        m = defaultdict(list)

        def dfs(node, level, m):
            if not node:
                return
            m[level].append(node)
            dfs(node.left, level + 1, m)
            dfs(node.right, level + 1, m)

        dfs(root, 0, m)
        for k in m:
            for i in range(1, len(m[k])):
                m[k][i-1].nextRight = m[k][i]



