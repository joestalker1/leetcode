# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def reverseBetween(self, head, m: int, n: int):
        if not head or m <= 0 or n <= 0 or m >= n:
            return head
        prefix = head
        i = 0
        #point to m-th
        while i < m - 2:
            prefix = prefix.next
            i += 1

        if m > 1:
            cur = prefix.next
        else:
            cur = head
        suc = cur.next
        i = m
        while i < n:
            t = suc.next
            suc.next = cur
            cur = suc
            suc = t
            i += 1

        if m == 1:
            t = head
            head = cur
            t.next = suc
        else:
            t = suc.next
            t.next = suc
            prefix.next = cur
        return head


sol = Solution()
a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(3)
a.next.next.next = ListNode(4)
a.next.next.next.next = ListNode(5)
b = sol.reverseBetween(a, 1, 5)