class Solution(object):
    def findNumberOfLIS(self, nums):
        if not nums:
            return 0
        dp = [0] * len(nums)
        count = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    if dp[j] >= dp[i]:
                        dp[i] = dp[j] + 1
                        count[i] = count[j]
                    elif dp[j] + 1 == dp[i]:
                        count[i] += count[j]
        max_len = max(dp)
        return sum([c for i,c in enumerate(count) if dp[i] == max_len])


sol = Solution()
arr = [12,17,76,32,11,17,94,-7,-23,40,86,71,45,63,98,30,-99,81,13,-9,27,43,24,99,51,96,12,-66,4,70,60,37,39,88,49,80,-75,49,29,13,-49,20,62,94,96,29,70,65,45,89,36,-19,-20,62,90,66,-79,-84,53,71,11,68,44,80,16,50,71,0,36,79,81,71,-69,69,76,37,9,87,25,-67,69,91,26,50,-71,18,71,-29,16,62,-10,51,67,4,14,75,24,-17,37,71,64,22,48,-4,9,29,25,11,7,73,97,-72,16,87,64,54,90,-88,5,26,-47,62,47,83,-59,85,86,35,70,47,87,75,-74,48,96,81,96,60]
#print(sol.findNumberOfLIS(arr))
#print(sol.findNumberOfLIS([2,2,2,2,2]))
print(sol.findNumberOfLIS([1,3,5,4,7]))

