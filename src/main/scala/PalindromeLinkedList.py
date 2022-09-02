# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head) -> bool:
        if not head:
            return True

        def find_half(node):
            fast = node
            slow = node
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        def reverse_list(node):
            prev = None
            cur = node
            while cur:
                t = cur.next
                cur.next = prev
                prev = cur
                cur = t
            return prev

        head1 = find_half(head)
        rev1 = reverse_list(head1)
        run = True
        a = rev1
        b = head
        while run and a and b:
            if a.val != b.val:
                run = False
            a = a.next
            b = b.next
        head1.next = reverse_list(rev1)
        return run