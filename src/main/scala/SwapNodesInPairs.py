# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def swapPairs(self, node):
        if not node or not node.next:
            return node
        p = None
        if node.next.next:
            p = self.swapPairs(node.next.next)
        #swap 2 nodes
        cur = node.next
        prev = node
        cur.next = prev
        prev.next = p
        return cur
