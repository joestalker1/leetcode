# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        new_head = None
        ptr = head
        # create new list A->A'->B->B'...
        while ptr:
            ptr_next = ptr.next
            ptr.next = Node(ptr.val,ptr_next)
            if not new_head:
                new_head = ptr.next
            ptr = ptr_next
        # set up random pointers for new list nodes
        ptr = head
        while ptr:
            if ptr.random:
                ptr.next.random = ptr.random.next
            ptr = ptr.next.next
        #reset intertwined lists
        ptr = head
        while ptr:
            ptr_next = ptr.next
            if ptr.next:
                ptr.next = ptr.next.next
            ptr = ptr_next
        return new_head


