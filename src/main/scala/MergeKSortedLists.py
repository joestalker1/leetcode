# Definition for singly-linked list.
from heapq import heappop,heappush

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists):
        min_heap = []
        for lst in lists:
            head = lst
            while head:
                heappush(min_heap, head.val)
                head = head.next
        head = ListNode(-1)
        node = head
        while min_heap:
            a = heappop(min_heap)
            node.next = ListNode(a)
            node = node.next
        return head.next
# [[-1,1],[-3,1,4],[-2,-1,0,2]]

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
