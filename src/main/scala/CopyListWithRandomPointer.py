# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

class Solution:
    def __init__(self):
        self.visited = {}

    def copy_node(self, node):
        if node:
            if node in self.visited:
                return self.visited[node]
            self.visited[node] = Node(node.val, None, None)
            return self.visited[node]
        return None

    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        p = head
        new_head = self.copy_node(p)
        while p:
            new_head.next = self.copy_node(p.next)
            new_head.random = self.copy_node(p.random)
            new_head = new_head.next
            p = p.next
        return self.visited[head]


