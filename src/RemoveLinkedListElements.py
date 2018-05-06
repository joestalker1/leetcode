class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None


class Solution(object):
    def removeElements(self, head, val):
        if not head:
            return
        plist = head
        prev = None
        while plist:
            if plist.val == val:
                if not prev:
                    head = plist.next
                else:
                    prev.next = plist.next
            else:
                prev = plist
            plist = plist.next
        return head


sol = Solution()
l1 = ListNode(1)
l1.next = ListNode(1)
print(sol.removeElements(l1, 1))
