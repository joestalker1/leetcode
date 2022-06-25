class Node:
    def __init__(self, key, val, nxt=None):
        self.key = key
        self.val = val
        self.next = nxt


class Bucket:
    def __init__(self):
        self.head = Node(-1, -1)

    def get(self, key):
        if not self.contains(key):
            return None
        cur = self.head.next
        while cur:
            if cur.key == key:
                return cur
            cur = cur.next
        return None

    def add(self, key, val):
        if not self.contains(key):
            node = Node(key, val, self.head.next)
            self.head.next = node
        else:
            node = self.get(key)
            node.val = val

    def remove(self, key):
        prev = self.head
        cur = self.head.next
        while cur:
            if cur.key == key:
                prev.next = cur.next
                return
            prev = cur
            cur = cur.next

    def contains(self, key):
        cur = self.head.next
        while cur:
            if cur.key == key:
                return True
            cur = cur.next
        return False


class MyHashMap:

    def __init__(self):
        self.key_space = 769
        self.array = [Bucket()] * self.key_space

    def _hash(self, key):
        return key % self.key_space

    def put(self, key: int, value: int) -> None:
        i = self._hash(key)
        self.array[i].add(key, value)

    def get(self, key: int) -> int:
        i = self._hash(key)
        node = self.array[i].get(key)
        return node.val if node else -1

    def remove(self, key: int) -> None:
        i = self._hash(key)
        self.array[i].remove(key)

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)