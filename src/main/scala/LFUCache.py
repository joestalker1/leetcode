from collections import defaultdict,OrderedDict


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1

class LFUCache:
    def __init__(self, capacity):
        self.vals = {}
        self.freq = defaultdict(OrderedDict)
        self.capacity = capacity
        self.min_freq = 1

    def _update(self, node):
        freq = node.freq
        self.freq[freq].pop(node.key)
        if freq == self.min_freq and not self.freq[freq]:
            self.min_freq += 1
        node.freq += 1
        self.freq[node.freq][node.key] = node

    def get(self, key):
        if key not in self.vals:
            return -1
        node = self.vals[key]
        self._update(node)
        return node.value

    def put(self, key, value):
        if self.capacity == 0:
            return
        if key in self.vals:
            node = self.vals[key]
            self._update(node)
            node.value = value
        else:
            if len(self.vals) == self.capacity:
                #pop up the oldest item
                _,node = self.freq[self.min_freq].popitem(last=False)
                del self.vals[node.key]
            node = Node(key, value)
            self.vals[key] = node
            self.freq[node.freq][node.key] = node
            self.min_freq = node.freq