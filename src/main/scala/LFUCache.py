from collections import defaultdict


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None


class DLinkedList:
    def __init__(self):
        self.sentinel = Node(None, None)
        self.size = 0
        self.sentinel.next = self.sentinel.prev = self.sentinel

    def __len__(self):
        return self.size

    def append(self, node):
        node.next = self.sentinel.next
        node.next.prev = node
        node.prev = self.sentinel
        #sentinel.prev -> last node(first appended node)
        self.sentinel.next = node
        self.size += 1

    def pop(self, node=None):
        if self.size == 0:
            return
        if not node:
            node = self.sentinel.prev

        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
        return node


class LFUCache:

    def __init__(self, capacity):
        self.vals = dict()
        self.freq = defaultdict(DLinkedList)
        self.capacity = capacity
        self.min_freq = 0
        self.size = 0

    def update(self, node):
        freq = node.freq
        self.freq[freq].pop(node)
        if freq == self.min_freq and not self.freq[freq]:
            self.min_freq += 1

        node.freq += 1
        freq = node.freq
        self.freq[freq].append(node)

    def get(self, key):
        if self.size == 0 or key not in self.vals:
            return -1

        node = self.vals[key]
        self.update(node)
        return node.value

    def put(self, key, value):
        if self.capacity == 0:
            return
        if key in self.vals:
            node = self.vals[key]
            self.update(node)
            node.value = value
        else:
            if self.size == self.capacity:
                node = self.freq[self.min_freq].pop()
                del self.vals[node.key]
                self.size -= 1
            node = Node(key, value)
            self.size += 1
            self.vals[key] = node
            self.freq[1].append(node)
            self.min_freq = 1



cache = LFUCache(2)
cache.put(3,1)
cache.put(2,1)
cache.put(2,2)
cache.put(4,4)
print(cache.get(2))#2

# cache = LFUCache(2)
# cache.put(1, 1)
# cache.put(2, 2)
# print(cache.get(1))  # returns 1
# cache.put(3, 3)  # evicts key 2
# print(cache.get(2))  # returns -1 (not found)
# print(cache.get(3))  # returns 3.
# cache.put(4, 4)  # evicts key 1.
# print(cache.get(1))  # returns -1 (not found)
# print(cache.get(3))  # returns 3
# print(cache.get(4))  # returns 4
