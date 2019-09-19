# Definition for singly-linked list.
from utils import *

class Solution:
    def copy_list(self, head):
        p = head
        new_head = None
        new_p = None
        while p:
            if not new_head:
                new_head = ListNode(p.val)
                new_p = new_head
            else:
                new_p.next = ListNode(p.val)
                new_p = new_p.next
            p = p.next
        return new_head

    def go(self, head, step):
        p1 = head
        while p1 and step > 0:
            p1 = p1.next
            step -= 1
        return p1

    def merge_sort(self, head, list_len, size):
        p0 = head
        p1 = self.go(p0, size)
        new_head = None
        pn = None
        while p0 or p1:
            if p0 and p1:
                #merge both sublists in ascending order
                sz0 = size
                sz1 = size if list_len >= 2 * size else list_len - size
                while p0 and p1 and sz0 > 0 and sz1 > 0:
                    if p0.val > p1.val:
                        new_node = ListNode(p1.val)
                        if not new_head:
                            new_head = new_node
                            pn = new_head
                        else:
                            pn.next = new_node
                            pn = pn.next
                        sz1 -= 1
                        p1 = p1.next
                    else:
                        new_node = ListNode(p0.val)
                        if not new_head:
                            new_head = new_node
                            pn = new_head
                        else:
                            pn.next = new_node
                            pn = pn.next
                        sz0 -= 1
                        p0 = p0.next
                if sz0 > 0:
                    while sz0 and p0:
                        pn.next = ListNode(p0.val)
                        pn = pn.next
                        p0 = p0.next
                        sz0 -= 1
                if sz1 > 0:
                    while sz1 and p1:
                        pn.next = ListNode(p1.val)
                        pn = pn.next
                        p1 = p1.next
                        sz1 -= 1
            elif p0 or p1:
                if not new_head:
                    new_head = self.copy_list(p0) if p0 else self.copy_list(p1)
                    pn = new_head
                else:
                    pn.next = self.copy_list(p0)
                    pn = pn.next
            p0 = p1
            p1 = self.go(p0, size)
        return new_head

    def sortList(self, head):
        if not head:
            return
        list_len = 0
        p0 = head
        while p0:
            list_len += 1
            p0 = p0.next
        size = 1
        while size <= list_len:
            head = self.merge_sort(head, list_len, size)
            size *= 2
        return head

#4->2->1->3
sol = Solution()
#[-1,5,3,4,0]
arr = [-84,142,41,-17,-71,170,186,183,-21,-76,76,10,29,81,112,-39,-6,-43,58,41,111,33,69,97,-38,82,-44,-7,99,135,42,150,149,-21,-30,164,153,92,180,-61,99,-81,147,109,34,98,14,178,105,5,43,46,40,-37,23,16,123,-53,34,192,-73,94,39,96,115,88,-31,-96,106,131,64,189,-91,-34,-56,-22,105,104,22,-31,-43,90,96,65,-85,184,85,90,118,152,-31,161,22,104,-85,160,120,-31,144,115]
list1 = arrayToListNode(arr)
#list1.next.next.next = ListNode(3)
list2 = sol.sortList(list1)
print(listNodeToArray(list2))
#[-1,5,3,4,0]

