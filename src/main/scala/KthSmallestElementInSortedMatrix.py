from collections import heapq

class Solution:
    def kthSmallest(self, matrix, k: int) -> int:
        if not matrix or not matrix[0]:
            return None
        n = len(matrix)
        m = len(matrix[0])
        min_heap = []
        for i in range(n):
            min_heap.append((matrix[i][0], i, 0))
        heapq.heapify(min_heap)
        cur_cnt = 0
        res = 0
        while cur_cnt < k:
            min_val,r,c = heapq.heappop(min_heap)
            if c + 1 < m:
                heapq.heappush(min_heap, (matrix[r][c+1],r,c+1))
            res = min_val
            cur_cnt += 1
        return res