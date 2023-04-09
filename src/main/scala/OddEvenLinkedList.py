class Solution:
    def oddEvenList(self, head):
        if not head:
            return None
        even_head = even = head.next
        odd = odd_head = head
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return odd_head