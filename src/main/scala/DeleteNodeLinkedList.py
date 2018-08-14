class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None


class Solution(object):
    def deleteNode(self, node):
        last = None
        while node.next:
            node.val = node.next.val
            last = node
            node = node.next
        last.next = None


l1 = ListNode(0)
l1.next = ListNode(0)
l1.next.next = ListNode(0)
sol = Solution()
sol.deleteNode(l1)