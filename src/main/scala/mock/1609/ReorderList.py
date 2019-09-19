# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def reorderList(self, head):
        if not head:
            return
        nodes = []
        p0 = head
        while p0:
            nodes.append(p0)
            prev = p0
            p0 = p0.next
            prev.next = None
        i = 0
        j = len(nodes) - 1
        head = None
        p0 = None
        while i < j:
            if not head:
                head = nodes[i]
                head.next = nodes[j]
                p0 = nodes[j]
            else:
                p0.next = nodes[i]
                p0.next.next = nodes[j]
                p0 = nodes[j]
            i += 1
            j -= 1
        if i == j:
            p0.next = nodes[j]

sol = Solution()
list = ListNode(1)
list.next = ListNode(2)
list.next.next = ListNode(3)
#list.next.next.next = ListNode(4)
sol.reorderList(list)




