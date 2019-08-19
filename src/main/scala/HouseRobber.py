class Solution:
    def rob(self, nums):
        if not nums:
            return 0

        def rob_house(from_house, mem):
            if from_house >= len(nums):
                return 0

            if mem[from_house][len(nums) - 1] >= 0:
                return mem[from_house][len(nums) - 1]
            max_money = 0
            for i in range(from_house, len(nums)):
                money_robbed = nums[i]
                next_house = i + 2
                money_robbed += rob_house(next_house, mem)
                max_money = max(money_robbed, max_money)
            mem[from_house][len(nums) - 1] = max_money
            return max_money
        mem = [-1] * len(nums)
        for i in range(len(nums)):
            mem[i] = [-1] * len(nums)
        return rob_house(0, mem)

sol = Solution()
#print(sol.rob([1,3,1,3,100]))#103
#print(sol.rob([183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]))
print(sol.rob([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))
#print(sol.rob([6,6,4,8,4,3,3,10]))#27
#print(sol.rob([2,7,9,3,1]))
#print(sol.rob([1,2,3,1]))