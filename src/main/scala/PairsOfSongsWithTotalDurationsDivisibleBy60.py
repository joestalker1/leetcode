class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        if len(time) < 2:
            return 0
        #count frequency of t % 60
        freq = [0] * 60
        pairs = 0
        for t in time:
            # if a % 60 + b % 60 = 0
            if t % 60 == 0:
                pairs += freq[0]
            else:
                # a % 60 + b % 60 = 60, a != 0
                pairs += freq[60 - t % 60]
            #update frequency for t % 60
            freq[t % 60] += 1
        return pairs