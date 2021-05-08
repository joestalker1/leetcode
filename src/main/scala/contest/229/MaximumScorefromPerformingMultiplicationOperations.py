class Solution:
    def maximumScore(self, nums, multipliers):
        mem = {}
        def find_max(l, r, i, mem):
            if (l,r,i) in mem:
                return mem[(l,r,i)]
            if l > r or i == len(multipliers):
                return 0
            max_score = nums[l] * multipliers[i] + find_max(l + 1, r, i + 1, mem)
            max_score = max(max_score, nums[r] * multipliers[i] + find_max(l, r - 1,i + 1, mem))
            mem[(l,r,i)] = max_score
            return max_score
        return find_max(0, len(nums) - 1, 0, mem)


sol = Solution()
print(sol.maximumScore(nums = [1,2,1], multipliers = [2,1]))#14
print(sol.maximumScore(nums = [-5,-3,-3,-2,7,1], multipliers = [-10,-5,3,4,6])) # 102


