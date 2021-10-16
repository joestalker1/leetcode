class Solution:
    def minElements(self, nums, limit: int, goal: int):
        sums = sum(nums)
        need = goal - sums
        cnt = abs(need) // limit
        if abs(need) % limit > 0:
            cnt += 1
        return cnt
