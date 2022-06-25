from collections import deque

class Solution:
    def widthOfBinaryTree(self, root) -> int:
        if not root:
            return 0
        queue = deque()
        queue.append((root,0))
        max_width = 0
        while queue:
            cur_len = len(queue)
            first = queue[0][1]
            for _ in range(cur_len):
                node,index = queue.popleft()
                if node.left:
                    queue.append((node.left,2*index))
                if node.right:
                    queue.append((node.right, 2*index + 1))
                max_width = max(max_width,index - first + 1)
        return max_width
