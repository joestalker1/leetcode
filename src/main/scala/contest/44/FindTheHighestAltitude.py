class Solution:
    def largestAltitude(self, gain):
        if not gain:
            return 0
        last_gain = 0
        res = []
        for i in range(len(gain)):
            res.append(last_gain + gain[i])
        return max(res)