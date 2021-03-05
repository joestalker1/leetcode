import math

from heapq import heappop, heappush,heapify

class Solution:
    def minimumDeviation(self, nums):
        n = len(nums)
        min_dev = math.inf
        min_val = math.inf
        q = []
        # increase all item till their maximal values
        for i in range(n):
            if nums[i] % 2 == 0:
                q.append(-nums[i])
                min_val = min(min_val, nums[i])
            else:
                q.append(-nums[i] * 2)
                min_val = min(min_val, nums[i] * 2)
        heapify(q)
        #max queue
        while q:
            # take max value
            a = -heappop(q)
            # calculate minimal deviation
            min_dev = min(min_dev, a - min_val)
            if a % 2 == 0:
                # a is even, we can decrease it
                min_val = min(min_val, a // 2)
                heappush(q, -a // 2)
            else:
                # if max is odd, we can't decrease it, so exit
                break
        return min_dev


sol = Solution()
print(sol.minimumDeviation([900,241,842,374,758,39,687,242,912]))#609
print(sol.minimumDeviation([4,1,5,20,3]))#3
print(sol.minimumDeviation([399,908,648,357,693,502,331,649,596,698]))#315
print(sol.minimumDeviation([2,8,6,1,6]))#1
print(sol.minimumDeviation([2,10,8]))#3
print(sol.minimumDeviation([1,2,3,4]))#1
print(sol.minimumDeviation([4,1,5,20,3]))#3



