class Solution:
    def lowestCommonAncestor(self, node: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not node:
            return None
        cur = node
        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                break
        return cur
