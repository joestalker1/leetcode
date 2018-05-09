class TreeNode:
    def __init__(self, n):
        self.val = n
        self.left = None
        self.right = None


class Solution:
    def wrap(self, s):
        return '(' + s + ')'

    def tree2str(self, root):
        if not root:
            return ''
        s = str(root.val)
        if root.left and root.right:
            s += self.wrap(self.tree2str(root.left)) + self.wrap(self.tree2str(root.right))
        elif root.left:
            s += self.wrap(self.tree2str(root.left))
        elif root.right:
            s += '()' + self.wrap(self.tree2str(root.right))
        return s


# 1 (2(4)()) (3()())

# 1(2(4()())())(3()())
# "1(2(4)())(3()())"
sol = Solution()
t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t1.left = t2
t1.right = t3
t2.left = t4
print(sol.tree2str(t1))
