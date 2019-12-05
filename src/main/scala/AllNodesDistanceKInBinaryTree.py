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

        parent = {}
        children = {}
        self.traverse(parent, children, root)

        def collect_nodes_below(v, dist, res):
            if dist == K:
                res.append(v)
                return
            if v in children:
                for child in children:
                    collect_nodes_below(child, dist + 1, res)

        def collect_nodes_above(v, dist, res):
            if dist == K:
                res.append(v)
                return
            if v in parent:
                collect_nodes_above(parent[v], dist + 1, res)
            else:
                # go down
                if dist < K:
                    collect_nodes_below(root.val, dist + 1, res)

        res = []
        # all nodes are below target
        collect_nodes_below(target.val, 0, res)
        # all nodes are above the target
        collect_nodes_above(target.val, 0, res)
        return res


arr = [3,5,1,6,2,0,8,None,None,7,4]#[7,4,1]
#arr = [0,1, None,3,2]
#arr=[1]
tree = arrayToTreeNode(arr)
sol = Solution()
print(sol.distanceK(tree,tree.left, 2))



