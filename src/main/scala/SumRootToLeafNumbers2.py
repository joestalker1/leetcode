from utils import TreeNode, arrayToTreeNode
from functools import reduce

class Solution:
    def to_num(self, digits):
        if len(digits) == 0:
            return 0
        chars = [chr(ord('0') + x) for x in digits]
        return int(reduce(lambda x,y:x+y,chars))

    def sumNumbers(self, root):
        if not root:
            return 0
        self.sum = 0

        def dfs(node, digits=[]):
            if not node:
               return
            if not node.left and not node.right:
                digits.append(node.val)
                num = self.to_num(digits)
                self.sum += num
                return
            another_digits = digits[:]
            another_digits.append(node.val)
            dfs(node.left, another_digits)
            digits.append(node.val)
            dfs(node.right, digits)
        dfs(root)
        return self.sum


sol = Solution()
print(sol.sumNumbers(None))
print(sol.sumNumbers(arrayToTreeNode([4,9,0,5,1])))
print(sol.sumNumbers(arrayToTreeNode([1,2,3])))

        



