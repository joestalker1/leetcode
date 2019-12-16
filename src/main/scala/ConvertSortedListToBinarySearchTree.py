# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedListToBST(self, head):
        if not head:
            return None
        arr = []
        node = head
        while node:
            arr.append(node.val)
            node = node.next

        def build_tree(arr, s, e):
            if s > e:
                return None
            # find middle
            m = (s + e) // 2
            new_node = TreeNode(arr[m])
            if s == e:
                return new_node
            new_node.left = build_tree(arr,s, m - 1)
            new_node.right = build_tree(arr,m + 1, e)
            return new_node
        return build_tree(arr, 0, len(arr) - 1)

def array_to_list(arr):
    head = node = ListNode(arr[0])
    for i in range(1, len(arr)):
        node.next = ListNode(arr[i])
        node = node.next
    return head


sol = Solution()

print(sol.sortedListToBST(array_to_list([-10,-3,0,5,9])))

