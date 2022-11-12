from collections import defaultdict

class Solution:
    def maxScoreIndices(self, nums):
        if not nums:
            return []
        nums_len = len(nums)
        pr_zero = [0] * (nums_len + 1)
        pr_one = [0] * (nums_len + 1)
        for i in range(nums_len):
            pr_zero[i+1] = pr_zero[i]
            pr_one[i+1] = pr_one[i]
            if nums[i] == 0:
                pr_zero[i+1] += 1
            if nums[i] == 1:
                pr_one[i+1] += 1
        div_to_index = defaultdict(list)
        for i in range(nums_len + 1):
            if i == 0:
                div_to_index[pr_one[-1]].append(0)
            elif i == nums_len:
                div_to_index[pr_zero[-1]].append(i)
            else:
                left_div = pr_zero[i]
                right_div = pr_one[nums_len] - pr_one[i]
                div_to_index[left_div+right_div].append(i)
        max_div = max(div_to_index)
        return div_to_index[max_div]


sol = Solution()
print(sol.maxScoreIndices([1,0,1,0,1,1,0,1,0]))#[4,0,2]
