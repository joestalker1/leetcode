from math import inf

class Solution:
    def maxScoreSightseeingPair(self, values) -> int:
        min_val_with_ind = values[0]
        max_score = -inf
        for i in range(1, len(values)):
            max_score = max(max_score, values[i] + min_val_with_ind - i)
            min_val_with_ind = max(min_val_with_ind, values[i] + i)
        return max_score
