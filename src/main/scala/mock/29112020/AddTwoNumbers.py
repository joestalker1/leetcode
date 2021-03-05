# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        if not l1 and not l2:
            return None
        if not l1:
            return l2
        if not l2:
            return l1
        #digist in reverse order
        carry = 0
        p1 = l1
        p2 = l2
        #sentinel node
        res = ListNode(-1)
        p3 = res
        while p1 and p2:
            r = p1.val + p2.val + carry
            p3.next = ListNode(r % 10)
            carry = r // 10
            p3 = p3.next
            p1 = p1.next
            p2 = p2.next
        if p1 or p2:
            r = (p1.val if p1 else p2.val)+ carry
            p3.next = ListNode(r % 10)
            p3 = p3.next
            carry = r // 10
        if carry:
            p3.next = ListNode(carry)
        return res






