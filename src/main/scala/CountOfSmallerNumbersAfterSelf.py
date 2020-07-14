class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.lessThan = 0

class Solution:
    def countSmaller(self, nums):
        if not nums or len(nums) == 0:
            return nums
        counts = [0] * len(nums)

        def insert(root, val, i, counts):
            if root.val < val:
                if root.right:
                    counts[i] += root.lessThan + 1
                    insert(root.right,val, i, counts)
                else:
                    root.right = Node(val)
                    root.right.lessThan = counts[i] + root.lessThan + 1
                    counts[i] = root.right.lessThan
            else:
                if root.left:
                    insert(root.left, val, i, counts)
                else:
                    root.left = Node(val)
        root = None
        for i in range(len(nums) - 1,-1,-1):
            if not root:
                root = Node(nums[i])
            else:
                insert(root,nums[i], i, counts)
        return counts



sol = Solution()
print(sol.countSmaller([7, 6, 1,1]))
print(sol.countSmaller([2, 0, 1]))
