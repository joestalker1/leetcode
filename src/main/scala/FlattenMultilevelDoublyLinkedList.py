"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        if not head:
            return None

        first = None
        last = None

        def add(node, last):
            if last:
                last.next = Node(node.val, last, None, None)
                return last.next
            return Node(node.val, None, None, None)

        def make_flat(node):
            nonlocal last, first
            if not node:
                return
            last = add(node, last)
            if not first:
                first = last
            if node.child:
                make_flat(node.child)
            make_flat(node.next)
        make_flat(head)
        return first

