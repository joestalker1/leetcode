class TreeNode:
    def __init__(self,v):
        self.val = v
        self.left = None
        self.right = None


class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """

        def generate_trees(start, end):
            if start > end:
                return [None, ]
            trees = []
            for i in range(start, end + 1):
                left = generate_trees(start, i - 1)
                right = generate_trees(i + 1, end)
                for l in left:
                    for r in right:
                        node = TreeNode(i)
                        node.left = l
                        node.right = r
                        trees.append(node)
            return trees

        trees = generate_trees(1, n)
        return trees if trees else None

        return generate_trees(1, n) if n else []


sol = Solution()
print(sol.generateTrees(3))