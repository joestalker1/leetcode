class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maximumAverageSubtree(self, root):
        if not root:
            return 0

        def find_avg(node):
            if not node:
                return [0, 0, 0] #count,sum, avg
            left_count,left_sum,left_avg = find_avg(node.left)
            right_count,right_sum,right_avg = find_avg(node.right)
            count = 1 + left_count + right_count
            sum_node = node.val + left_sum + right_sum
            avg = sum_node / count
            max_avg = max(avg, left_avg, right_avg)
            return [count, sum_node, max_avg]
        return find_avg(root)[2]

