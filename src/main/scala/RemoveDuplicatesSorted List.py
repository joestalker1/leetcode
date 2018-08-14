class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def skipIfEqual(self,cur, last, x):
        if not cur:
            return
        elif cur.val == x:
            if last.val == x:
                last.next = None
            cur.next = None
            self.skipIfEqual(cur.next, last, x)
        else:
            last.next = cur
            self.skipIfEqual(cur.next, cur, cur.val)



    def deleteDuplicates(self, head):
        if not head:
            return head
        self.skipIfEqual(head.next, head, head.val)
        return head


sol = Solution()
l1 = ListNode(1)
l2 = ListNode(1)
l1.next = l2
r = sol.deleteDuplicates(l1)
print(r)