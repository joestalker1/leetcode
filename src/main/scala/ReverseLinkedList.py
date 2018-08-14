class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def length(self, head):
        len1 = 0
        while head:
            len1 += 1
            head = head.next
        return len1

    def isPalindrome(self, head):
        if not head or not head.next:
            return True
        len1 = self.length(head)
        half = len1 // 2
        first = head
        p1 = head
        for i in range(half):
            p1 = p1.next
        if len1 & 0x1 == 1:
            second = p1.next
        else:
            second = p1
        prev = second
        second = second.next
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        second = prev
        for i in range(half):
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        return True


l1 = ListNode(1)
l1.next = ListNode(2)
#l1.next.next = ListNode(1)
#l1.next.next.next = ListNode(1)
sol = Solution()
print(sol.isPalindrome(l1))

