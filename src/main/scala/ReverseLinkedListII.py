# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def reverseBetween(self, head, m: int, n: int):
        if not head:
            return None
        cur = head
        prev = None
        while m > 1:
            prev = cur
            cur = cur.next
            m -= 1
            n -= 1
        con = prev
        tail = cur
        while n:
            t = cur.next
            cur.next = prev
            prev = cur
            cur = t
            n -= 1
        if con:
            con.next = prev
        else:
            head = prev
        tail.next = cur
        return head


sol = Solution()
a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(3)
a.next.next.next = ListNode(4)
a.next.next.next.next = ListNode(5)
b = sol.reverseBetween(a, 1, 5)