class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        q = [start]
        min_op = 0
        seen = set()
        while q:
            cur_len = len(q)
            for i in range(cur_len):
                x = q.pop(0)
                if x == goal:
                    return min_op
                for num in nums:
                    for cand in (x + num,x - num,x ^ num):
                        if cand not in seen and (0 <= cand <= 1000 or cand == goal):
                            q.append(cand)
                            seen.add(cand)
            min_op += 1
        return -1
