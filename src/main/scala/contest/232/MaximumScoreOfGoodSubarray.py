class Solution:
    def maximumScore2(self, nums, k):
        if not nums:
            return None
        l = k
        r = k
        n = len(nums)
        min_val = nums[k]
        score = nums[k]
        while l > 0 or r < n - 1:
            if l == 0:
                r += 1
            elif r == n - 1:
                l -= 1
            elif nums[l - 1] < nums[r + 1]:
                r += 1
            else:
                l -= 1
            min_val = min(min_val, nums[l], nums[r])
            score = max(score, min_val * (r - l + 1))
        return score

    def maximumScore(self, nums, k):
        if not nums:
            return None
        l = k
        r = k
        n = len(nums)
        min_val = nums[k]
        score = nums[k]
        while l > 0 or r < n - 1:
            if l == 0:

            if l > 0 and r < n - 1:
                if nums[l] > nums[r]:
                    l -= 1
                else:
                    r += 1
            elif l > 0:
                l -= 1
            elif r < n -1:
                r += 1
            else:
                break
            min_val = min(min_val, nums[l],nums[r])
            score = max(score, min_val * (r - l + 1))
        return score

sol = Solution()
print(sol.maximumScore([6569,9667,3148,7698,1622,2194,793,9041,1670,1872], 5))#9732