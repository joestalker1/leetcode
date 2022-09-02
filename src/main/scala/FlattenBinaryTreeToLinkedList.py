class Solution:
    def flatten(self, root) -> None:
        if not root:
            return None
        head = None

        def flatten(node):
            nonlocal head
            if not node:
                return
            flatten(node.right)
            flatten(node.left)
            node.right = head
            node.left = None
            head = node

        flatten(root)
        return head