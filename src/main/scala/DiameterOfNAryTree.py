"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""


class Solution:
    def diameter(self, root: 'Node') -> int:
        if not root:
            return 0

        longest_diameter = 0

        def find_longest_diameter(node):
            nonlocal longest_diameter
            if not node:
                return 0
            longest_branch_len1 = 0
            longest_branch_len2 = 0
            for child in node.children:
                branch_len = find_longest_diameter(child) + 1
                if branch_len > longest_branch_len1:
                    longest_branch_len2 = max(longest_branch_len2, longest_branch_len1)
                    longest_branch_len1 = branch_len
                elif branch_len > longest_branch_len2:
                    longest_branch_len2 = branch_len
            longest_diameter = max(longest_diameter, longest_branch_len1 + longest_branch_len2)
            return longest_branch_len1

        find_longest_diameter(root)
        return longest_diameter