class Node:
    def __init__(self, name):
        self.name = name
        self.children = {}
        self.is_delete = False


class Solution:
    def deleteDuplicateFolder(self, paths):

        def build_tree(root, path):
            for p in path:
                if p not in root.children:
                    node = Node(p)
                    root.children[p] = node
                root = root.children[p]

        def dedupe(root, seen):
            sub = ''
            if not root:
                return sub
            for name in root.children:
                sub += dedupe(root.children[name], seen)
            if len(sub):
                if sub in seen:
                    root.is_delete = seen[sub].is_delete = True
                else:
                    seen[sub] = root
            return '(' + root.name + sub + ')'

        def get_path(root, path, res):
            if not root or root.is_delete:
                return
            path.append(root.name)
            res.append(path[::])
            for name in root.children:
                get_path(root.children[name], path, res)
            path.pop()

        paths.sort(key=lambda x: (-len(x), x[-1]))
        seen = {}
        root = Node('')
        for path in paths:
            build_tree(root, path)
        dedupe(root, seen)
        res = []
        path = []
        for name in root.children:
            get_path(root.children[name], [], res)
        return res
