from utils import *

class Solution:
    def insertionSortList(self, head):
        if not head:
            return None
        new_head = None
        p0 = head
        while p0:
            if not new_head:
                new_head = ListNode(p0.val)
            else:
                p1 = new_head
                prev = None
                while p1 and p1.val <= p0.val:
                    prev = p1
                    p1 = p1.next
                if not prev:
                    t = new_head
                    new_head = ListNode(p0.val)
                    new_head.next = t
                else:
                    t = prev.next
                    prev.next = ListNode(p0.val)
                    prev.next.next = t
            p0 = p0.next
        return new_head

sol = Solution()


