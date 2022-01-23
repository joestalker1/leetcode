class Tree:
    def __init__(self, id, a):
        self.id = id
        self.a = a
        self.left = None
        self.right = None

    def succ(self, k):
        if k == 0:
            return self
        n1 = self.succ(k - 1)
        n2 = self.succ(k - 1)
        return n1 if n1 else n2

    # need to implement it!
    def preprocess(self, k):
        self.anc = [0] * self.n
        for i in range(self.n):
            self.anc[i] = {}
        for x in self.vertices:
            a = 1
            while a <= k:
                self.prep[x][a] = self.succ(x, a)
                a = a << 1

    # need to implement it!
    def ancestor(self, x, k):
        log2 = int(log(k, 2))
        suc = x
        while k > 0:
            b = 2 ** log2
            suc = self.prep[suc][b]
            k -= b
            if k > 0:
                log2 = int(log(k, 2))



class SubtreeQueries:
    def __init__(self, tree):
        nodes = []
        self.tree = tree
        self.dfs(tree, nodes)
        self.data = []
        for i in range(len(nodes)):
            sz = self.dfs(nodes[i], [])
            self.data.append((nodes[i].id, sz, nodes[i].a))

    def dfs(self, node, buf):
        if not node:
            return 0
        buf.append(node)
        n1 = self.dfs(node.left, buf)
        n2 = self.dfs(node.right, buf)
        return 1 + n1 + n2

    def sum_of_subtree(self, id):
        for i in range(len(self.data)):
            if self.data[i][0] == id:
                sz = self.data[i][1]
                subarr = self.data[i:i + sz]
                return sum(r[2] for r in subarr)
        return 0

    def depth(self, node, id, k):
        if not node:
            return k
        if node.id == id:
            return k
        n1 = self.depth(node.left, id, k + 1)
        if n1:
            return n1
        return self.depth(node.rigth, id, k + 1)


    def distance(self, id1, id2):
        d1 = self.depth(self.tree, id1, 1)
        d2 = self.depth(self.tree, id2, 1)
        lca = LowestCommonAncestor(self.tree)
        res = lca.find(id1, id2)
        return d1 + d2 - 2 * self.depth(self.tree, res, 1)



class LowestCommonAncestor:
    def __init__(self, tree):
        self.data = []
        self.dfs(tree, self.data, 1)

    def dfs(self, node, buf, k):
        if not node:
            return
        buf.append((node.id, k))

        if node.left:
            self.dfs(node.left, buf, k + 1)
            buf.append((node.id, k))

        if node.right:
            self.dfs(node.right, buf, k + 1)
            buf.append((node.id, k))

    def find(self, id1, id2):
        i1 = 0
        i2 = 0
        for i in range(len(self.data)):
            if self.data[i][0] == id1:
                i1 = i
                break
        for i in range(i+1, len(self.data)):
            if self.data[i][0] == id2:
                i2 = i
                break

        min_depth = float("inf")
        res = 0
        for j in range(i1, i2 + 1):
            if self.data[j][1] < min_depth:
                res = self.data[j][0]
                min_depth = self.data[j][1]
        return res


root = Tree(1, 1)
root.left = Tree(2, 2)
root.right = Tree(4, 4)
root.left.left = Tree(5, 5)
root.left.right = Tree(6, 6)
root.left.right.left = Tree(8, 8)
root.right.left = Tree(7, 7)

subtree = SubtreeQueries(root)
print(subtree.sum_of_subtree(4))
print(subtree.distance(5, 8))

lca = LowestCommonAncestor(root)
print(lca.find(2, 4))
print(lca.find(5, 8))