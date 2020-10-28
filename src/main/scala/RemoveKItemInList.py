class Node:
    def __init__(self, val, nxt=None):
        self.val = val
        self.next = nxt


def print_ll(head):
    s = ''
    curr = head
    while curr is not None:
        s += str(curr.val)
        s += '->'
        curr = curr.next
    print(s)


def remove_kth_node_from_end(head, k):
    fast = head
    for i in range(k):
        fast = fast.next

    slow = head
    while fast.next is not None:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next