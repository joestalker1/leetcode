from collections import defaultdict

class Solution:
    def isPossible(self, nums):
        av = defaultdict(int)
        # count subsequence value
        want = defaultdict(int)
        for a in nums:
            av[a] += 1
        for i in range(len(nums)):
            a = nums[i]
            # no available values
            if av[a] <= 0:
                continue
            # if some suqsequence needs to have a
            if want[a] > 0:
                av[a] -= 1
                # mark that we've used a
                want[a] -= 1
                # request next value
                want[a+1] += 1
            # if it has minimal subsequence
            elif av[a] > 0 and av[a+1] > 0 and av[a+2] > 0:
                av[a] -= 1
                av[a+1] -= 1
                av[a+2] -= 1
                # request next value
                want[a+3] += 1
            else:
                return False
        return True