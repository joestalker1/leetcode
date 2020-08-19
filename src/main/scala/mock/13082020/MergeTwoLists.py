# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return l1
        if not l1:
            return l2
        if not l2:
            return l1
        new_list = ListNode()
        p1 = l1
        p2 = l2
        res = new_list
        while p1 and p2:
            if p1.val < p2.val:
                res.next = ListNode(p1.val)
                p1 = p1.next
            else:
                res.next = ListNode(p2.val)
                p2 = p2.next
            res = res.next
        while p1:
            res.next = ListNode(p1.val)
            res = res.next
            p1 = p1.next
        while p2:
            res.next = ListNode(p2.val)
            res = res.next
            p2 = p2.next
        return new_list.next

