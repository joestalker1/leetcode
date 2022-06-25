class Solution:
    def connect(self, root: 'Node') -> 'Node':

        def process_child(child, prev, leftmost):
            if child:
                # next level
                if prev:
                    prev.next = child
                else:
                    leftmost = child
                prev = child
            return prev, leftmost

        if not root:
            return root
        leftmost = root
        while leftmost:
            prev = None
            cur = leftmost
            leftmost = None
            while cur:
                prev, leftmost = process_child(cur.left, prev, leftmost)
                prev, leftmost = process_child(cur.right, prev, leftmost)
                cur = cur.next
        return root