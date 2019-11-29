from random import choice

class Solution(object):

    def __init__(self, nums):
        self.num_freq = {a:[] for a in nums}
        for i,a in enumerate(nums):
            self.num_freq[a].append(i)

    def pick(self, target):
        if len(self.num_freq[target]) == 1:
            return self.num_freq[target][0]
        freq = self.num_freq[target]
        return choice(freq)