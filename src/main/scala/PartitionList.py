# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def partition(self, head, x: int):
        if not head:
            return head
        before = before_head = ListNode(-1)
        after = after_head = ListNode(-1)
        p = head
        while p:
            if p.val < x:
                before.next = p
                before = before.next
            else:
                after.next = p
                after = after.next
            p = p.next
        before.next = after_head.next
        after.next = None
        return before_head.next

list1 = ListNode(1)
#list1.next = ListNode(1)
list1.next = ListNode(4)
list1.next.next = ListNode(3)
list1.next.next.next = ListNode(2)
list1.next.next.next.next = ListNode(5)
list1.next.next.next.next.next = ListNode(2)
sol = Solution()
sol.partition(list1, 3)


