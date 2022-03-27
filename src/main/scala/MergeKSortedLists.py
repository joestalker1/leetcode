# Definition for singly-linked list.
from heapq import heappop,heappush

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# [[-1,1],[-3,1,4],[-2,-1,0,2]]
class Solution:
    def mergeKLists(self, lists):
        min_heap = []
        for lst in lists:
            if lst:
                heappush(min_heap, (lst.val, lst))
        p = sorted_lst = ListNode(-1)
        while min_heap:
            (val, lst) = heappop(min_heap)
            p.next = ListNode(val)
            p = p.next
            lst = lst.next
            if lst:
                heappush(min_heap, (lst.val, lst))
        return sorted_lst.next
def makeList(arr):
    head = ListNode(-1)
    node = head
    for a in arr:
        node.next= ListNode(a)
        node = node.next
    return head.next

lst1 = ListNode(-1)
sol = Solution()
print(sol.mergeKLists([makeList([-1,1]), makeList([-3,1,4]), makeList([-2,-1,0,2])]))
