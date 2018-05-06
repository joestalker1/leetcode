class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return
        l1 = headA
        l2 = headB
        c = 0
        while (l1 or l2) and c <= 2:
            if l1 == l2:
                return l1
            l1 = l1.next
            l2 = l2.next
            if not l1:
                l1 = headB
                c += 1
            if not l2:
                l2 = headA
                c += 1


sol = Solution()
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)

l2 = ListNode(0)
l2.next = l1.next.next

print(sol.getIntersectionNode(l2, l1).val)