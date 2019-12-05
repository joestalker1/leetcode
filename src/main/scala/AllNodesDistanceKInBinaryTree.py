from utils import TreeNode, arrayToTreeNode

class Solution(object):
    def traverse(self, parent, children, root):
        q = [root]
        while q:
            node = q.pop(0)
            if node.val not in children:
                children[node.val] = []
            if node.left:
                children[node.val].append(node.left.val)
                parent[node.left.val] = node.val
                q.append(node.left)
            if node.right:
                children[node.val].append(node.right.val)
                parent[node.right.val] = node.val
                q.append(node.right)

    def distanceK(self, root, target, K):
        if not root or not target:
            return None
        res = []
        parent = {}
        children = {}
        self.traverse(parent, children, root)


        if K in m:
            res += m[K]
        dist = self.distance(parent, root, target)
        if K - dist > 0:
            diff = K - dist
            m = self.traverse(root, target.val, diff)
            if diff in m:
                res += m[diff]
        return res



arr = [3,5,1,6,2,0,8,None,None,7,4]
arr = [0,1, None,3,2]
#arr=[1]
tree = arrayToTreeNode(arr)
sol = Solution()
print(sol.distanceK(tree,tree.left.right, 1))#[1]



