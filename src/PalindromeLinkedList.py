class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def check(self, head, cur):
        if not head.next:
            return (cur.val == head.val, cur.next)
        eq, next = self.check(head.next, cur)
        return (eq and head.val == next.val, next.next)

    def isPalindrome(self, head):
        if not head:
            return True
        p1 = head
        p2 = head
        while p2.next:
            p2 = p2.next

        res = self.check(head, head)
        return res[0]


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(2)
sol = Solution()
print(sol.isPalindrome(l1))
