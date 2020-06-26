class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class DLinkedList:
    def __init__(self):
        self.sentinel = Node(None, None)
        # prev points to last node
        self.sentinel.prev = self.sentinel.next = self.sentinel
        self.size = 0

    def __len__(self):
        return self.size

    def append(self, node):
        node.next = self.sentinel.next  # prev points to last
        node.next.prev = node
        node.prev = self.sentinel
        self.sentinel.next = node
        self.size += 1

    def pop(self, node=None):
        if self.size == 0:
            return None
        if not node:
            node = self.sentinel.prev
        self.size -= 1
        node.prev.next = node.next
        node.next.prev = node.prev
        return node



class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.vals = {}
        self.fifo = DLinkedList()

    def update(self, node):
        self.fifo.pop(node)
        self.fifo.append(node)

    def get(self, key: int):
        if key not in self.vals:
            return -1
        node = self.vals[key]
        self.update(node)
        return node.value

    def put(self, key, value):
        if key in self.vals:
            node = self.vals[key]
            self.update(node)
            node.value = value
        else:
            if self.capacity == len(self.fifo):
                lru = self.fifo.pop()
                del self.vals[lru.key]
            node = Node(key, value)
            self.vals[key] = node
            self.fifo.append(node)


["LRUCache","get","put","get","put","put","get","get"]
[[2],[2],[2,6],[1],[1,5],[1,2],[1],[2]]

cache = LRUCache(2)
cache.get(2)
cache.put(2,6)
cache.get(1)
cache.put(1,5)
cache.put(1,2)
cache.get(1)
print(cache.get(2))


# cache.put(1, 1)
# cache.put(2, 2)
# print(cache.get(1))       # returns 1
# cache.put(3, 3)    # evicts key 2
# print(cache.get(2))       # returns -1 (not found)
# cache.put(4, 4)    # evicts key 1
# print(cache.get(1))      # returns -1 (not found)
# print(cache.get(3))      # returns 3
# print(cache.get(4))      # returns 4