import utils
from utils import TreeNode


class Codec:
    def serialize(self, root):
        if not root:
            return None

        buf = []

        def rserialize(node, buf):
            if not node:
                buf.append('null')
                return
            buf.append(node.val)
            rserialize(node.left, buf)
            rserialize(node.right, buf)

        rserialize(root, buf)
        return '[' + ','.join([str(e) for e in buf]) + ']'

    def deserialize(self, data):
        if not data:
            return None

        def rdeserialize(buf):
            if not buf or buf[0] == 'null':
                if buf:
                    buf.pop(0)
                return None
            node = TreeNode(buf[0])
            buf.pop(0)
            node.left = rdeserialize(buf)
            node.right = rdeserialize(buf)
            return node

        data = data[1:-1].split(',')
        return rdeserialize(data)


codec = Codec()
arr = [1, 2, 3, None, None, 4, 5]
tree = utils.arrayToTreeNode(arr)
s = codec.serialize(tree)
tree2 = codec.deserialize(s)
