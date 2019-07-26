class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, head):
        if not head or not head.next:
            return
        p = head
        q = []
        while p:
            q.append(p)
            p = p.next
        p = head
        count = len(q) // 2
        if len(q) % 2 == 1:
            count += 1

        while count > 0:
            last = q.pop()
            last.next = None
            t = p.next
            p.next = last
            last.next = t
            p = t
            count -= 1
        if p:
            p.next = None

sol = Solution()
list1 = ListNode(1)
#list1.next = ListNode(2)
#list1.next.next = ListNode(3)
sol.reorderList(list1)
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(3)
list1.next.next.next= ListNode(4)
sol.reorderList(list1)
print(list1)










