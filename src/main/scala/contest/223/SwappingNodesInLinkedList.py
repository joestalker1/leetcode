# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: ListNode, k):
        n = 0
        p = head
        #count list length
        while p:
            n += 1
            p = p.next
        p1 = head
        for i in range(k):
            p1 = p1.next
        p2 = head
        for i in range(n - k):
            p2 = p2.next
        p1.val,p2.val = p2.val,p2.val
        return head



