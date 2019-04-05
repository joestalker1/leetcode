class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        if not head:
            return head

        def rev_list(h, p):
            if not h:
                return p
            new_head = rev_list(h.next, h)
            h.next = p
            if p:
                p.next = None
            return new_head

        return rev_list(head, None)

list = ListNode(1)
list.next = ListNode(2)
list.next.next = ListNode(3)
list.next.next.next = ListNode(4)

sol = Solution()
new_head = sol.reverseList(list)

print(new_head)


