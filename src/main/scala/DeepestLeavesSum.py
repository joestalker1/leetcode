class Solution:
    def deepestLeavesSum(self, root) -> int:
        q = [root]
        cur_sum = 0
        while q:
            sz = len(q)
            cur_sum = 0
            for i in range(sz):
                node = q.pop(0)
                cur_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return cur_sum