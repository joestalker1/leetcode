# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def partition(self, head, x):
        if not head:
            return
        min_p = None
        e1 = None
        max_p = None
        e2 = None
        cur = head
        while cur:
            if cur.val < x:
                if not min_p:
                    min_p = cur
                    e1 = min_p
                    cur = cur.next
                    e1.next = None
                else:
                    e1.next = cur
                    e1 = e1.next
                    cur = cur.next
                    e1.next = None
            else:
                if not max_p:
                    max_p = cur
                    e2 = max_p
                    cur = cur.next
                    e2.next = None
                else:
                    e2.next = cur
                    e2 = e2.next
                    cur = cur.next
                    e2.next = None
        if min_p and max_p:
            e1.next = max_p
            return min_p
        if min_p:
            return min_p
        return max_p


list1 = ListNode(1)
#list1.next = ListNode(1)
list1.next = ListNode(4)
list1.next.next = ListNode(3)
list1.next.next.next = ListNode(2)
list1.next.next.next.next = ListNode(5)
list1.next.next.next.next.next = ListNode(2)
sol = Solution()
sol.partition(list1, 3)


