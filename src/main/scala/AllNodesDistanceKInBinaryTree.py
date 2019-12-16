from utils import TreeNode, arrayToTreeNode

class Solution(object):
     def distanceK(self, root, target, K):
        if not root or not target:
            return None

        def dfs(node, par = None):
            if node:
                node.par = par
                dfs(node.left, node)
                dfs(node.right, node)
        dfs(root)
        q = [(target, 0)]
        seen = {target.val}
        while q:
            if q[0][1] == K:
                return [n.val for n,d in q]
            node,dist = q.pop(0)
            for n in (node.left, node.right, node.par):
                if n and n.val not in seen:
                    q.append((n, dist + 1))

        return []


sol = Solution()
# arr = [0, 1, None, None, 2, None, 3, None, 4]
# tree = arrayToTreeNode(arr)
# print(sol.distanceK(tree, tree.left.right.right, 0))#[3]
#
#
# arr = [0, 2, 1, None, None, 3]
# tree = arrayToTreeNode(arr)
# print(sol.distanceK(tree, tree.right.left, 3))#[2]

arr = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]  # [7,4,1]
tree = arrayToTreeNode(arr)
print(sol.distanceK(tree, tree.left, 2))
