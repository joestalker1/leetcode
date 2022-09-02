from collections import defaultdict,Counter

class Solution:
    def isPossible(self, nums) -> bool:
        if len(nums) < 3:
            return False
        # store last item freq of subseq an
        subseq = defaultdict(int)
        freq = Counter(nums)
        for i in range(len(nums)):
            if freq[nums[i]] == 0:
                continue
            # consider if nums[i] is last item in existing subseq or start item in new subsequence
            if subseq[nums[i] - 1] > 0:
                # decrease number of subseq ending by nums[i] - 1
                subseq[nums[i] - 1] -= 1
                # increase number by subseq ending by nums[i]
                subseq[nums[i]] += 1
            # if exist at least 3 lenght subsequence
            elif freq[nums[i] + 1] > 0 and freq[nums[i] + 2] > 0:
                subseq[nums[i] + 2] += 1
                freq[nums[i] + 1] -= 1
                freq[nums[i] + 2] -= 1
            else:
                return False
            freq[nums[i]] -= 1
        return True
