# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def len_list(self, l):
        if not l:
            return 0
        c = 0
        while l:
            c+=1
            l = l.next
        return c

    def add_zero_nodes(self, l, d):
        while d > 0:
            z = ListNode(0)
            z.next = l
            l = z
            d -= 1
        return l

    def addTwoNumbers(self, l1, l2):
        if not l1 or not l2:
            return None
        carry = 0
        res = None
        len1 = self.len_list(l1)
        len2 = self.len_list(l2)
        if len1 > len2:
            l2 = self.add_zero_nodes(l2, len1 - len2)
        elif len2 > len1:
            l1 = self.add_zero_nodes(l1, len2 - len1)

        def sum_list(p1, p2):
            nonlocal carry, res
            if not p1:
                return
            sum_list(p1.next, p2.next)
            a = p1.val + p2.val + carry
            carry = a // 10
            a = a % 10
            node = ListNode(a)
            if res:
                node.next = res
            res = node

        sum_list(l1, l2)
        if carry:
            node = ListNode(carry)
            node.next = res
            res = node
        return res
#(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)

list1 = ListNode(7)
list1.next = ListNode(2)
list1.next.next = ListNode(4)
list1.next.next.next = ListNode(3)

list2 = ListNode(5)
list2.next = ListNode(6)
list2.next.next = ListNode(4)

sol = Solution()
res = sol.addTwoNumbers(list1, list2)









