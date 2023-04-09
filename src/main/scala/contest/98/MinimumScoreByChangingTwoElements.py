import heapq


class Solution:
    def minimizeSum(self, nums) -> int:
        if len(nums) < 4:
            return 0
        min_heap = [nums[-1]]
        max_heap = [-nums[-1]]
        for i in range(len(nums) - 2, -1,-1):
            max_score = max(abs(nums[i] - min_heap[0]),abs(nums[i]+max_heap[0]))
            print('{} {}'.format(nums[i], max_score))
            heapq.heappush(min_heap, nums[i])
            heapq.heappush(max_heap, -nums[i])
        return 0
       #72,54,50,48
sol = Solution()
print(sol.minimizeSum([59,27,9,81,33]))#24
# 59
# 32 50 22 26
# 27
# 18 54 6
# 9
# 72 24
# 81
# 48
# 0