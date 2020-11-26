class Node(object):
    def __init__(self, val, lst):
        self.val = val
        self.children = lst


class Codec:
    def serialize(self, root: 'Node'):
        if not root:
            return None

        buf = []
        self._serialize(root, buf)
        return ''.join(buf)

    def _serialize(self, root, buf):
        if not root:
            return
        buf.append(chr(root.val + 48))
        buf.append(chr(len(root.children) + 48))
        for child in root.children:
            self._serialize(child, buf)

    def deserialize(self, data: str) -> 'Node':
        if not data:
            return None
        pos = [0]
        return self._deserialize(data, pos)

    def _deserialize(self, data, pos):
        if len(data) == pos[0]:
            return None
        val = ord(data[pos[0]]) - 48
        pos[0] += 1
        n = ord(data[pos[0]]) - 48
        node = Node(val, [])
        for _ in range(n):
            pos[0] += 1
            node.children.append(self._deserialize(data, pos))
        return node


codec = Codec()
# n = Node(3)
# n.children.append(Node(5))
# n.children.append(Node(6))
# r = Node(1)
# r.children.append(n)
# r.children.append(Node(2))
# r.children.append(Node(4))
# s = codec.serialize(r)
# print(s)
nr = codec.deserialize("[ 1 [ 3 [ 5 6 ] 2 4 ] ]")
print(nr)
