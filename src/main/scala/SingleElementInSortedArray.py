class Solution:
    def singleNonDuplicate(self, nums):
        lo = 0
        hi = len(nums) - 1
        #array shouldn't be sorted but should being pairing
        while lo < hi: # strict inequality
            m = lo + (hi-lo) // 2
            halves_is_even = (hi - m) % 2 == 0
            if nums[m] == nums[m+1]:
                # mid 's partner is to the right
                if halves_is_even:
                    lo = m + 2
                else:
                    hi = m - 1
            elif nums[m-1] == nums[m]:
                # mid partner is to the left
                if halves_is_even:
                    hi = m - 2
                else:
                    lo = m + 1
            else:
                return nums[m]
        return nums[lo]
