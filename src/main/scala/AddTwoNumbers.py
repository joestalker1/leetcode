# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def add_nums(self, res, l, carry):
        while l:
            a = l.val + carry
            carry = a // 10
            a = a % 10
            res.append(a)
            l = l.next
        return carry

    def addTwoNumbers(self, l1, l2):
        if not l1 or not l2:
            return []
        i = l1
        j = l2
        carry = 0
        res = []
        while i  and j:
            a = i.val + j.val + carry
            carry = a // 10
            a = a % 10
            res.append(a)
            i = i.next
            j = j.next
        if i:
            carry = self.add_nums(res, i, carry)
        if j:
            carry = self.add_nums(res, j, carry)
        if carry > 0:
            res.append(carry)

        return res

