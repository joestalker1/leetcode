class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def comp_val(self, root, a, b):
        if not root:
            return None
        res = None
        if root.val < a and root.val < b:
            self.comp_val(root.right, a, b)
        elif root.val > a and root.val > b:
            self.comp_val(root.left, root.left, a, b)
        else:
            return root



    def trace_path(self, root, a, path):
        if not root:
            return
        path.append(root.val)
        if a == root.val:
            return
        if root.val < a:
            self.trace_path(root.right, a, path)
        elif root.val > a:
            self.trace_path(root.left, a, path)

    def get_last_index_of_common_part(self, path1, path2):
        i = 0
        while i <len(min(path1, path2)):
            if path1[i] != path2[i]:
                return i - 1
            i += 1
        return i - 1


    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return None
        path1 = []
        self.trace_path(root, p, path1)
        path2 = []
        self.trace_path(root, q, path2)
        i = self.get_last_index_of_common_part(path1, path2)
        return path1[i] if i > -1 else None


sol = Solution()
root = TreeNode(2)
root.left = TreeNode(1)
print(sol.lowestCommonAncestor(root, 2, 1))



