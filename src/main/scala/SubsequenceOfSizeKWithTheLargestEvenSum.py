class Solution:
    def largestEvenSum(self, nums: List[int], k: int) -> int:
        # assert self._largestEvenSum([1,2,4], 2) == 6, 'test1'
        # assert self._largestEvenSum([3,2,3], 2) == 6, 'test2'
        # assert self._largestEvenSum([1,1,1], 1) == -1, 'test3'
        return self._largestEvenSum(nums, k)

    def _largestEvenSum(self, nums: List[int], k: int) -> int:
        if len(nums) < k:
            return -1
        min_heap = []
        for num in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap, num)
            else:
                if min_heap[0] < num:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, num)
        min_heap.sort(reverse=True)
        even_sum = 0
        min_even_odd = [inf, inf]
        for i in range(k):
            j = nums[i] % 2
            even_sum += min_heap[i]
            min_even_odd[j] = min(min_even_odd[j], min_heap[i])
        if even_sum % 2 == 0:
            return even_sum
        max_sum = -1
        for i in range(len(nums)):
            j = nums[i] % 2
            max_sum = max(max_sum, even_sum - min_even_odd[1 - j] + nums[i])
        return max_sum
    