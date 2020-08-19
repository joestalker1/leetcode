class NumArray:

    def __init__(self, nums):
        self.prefix = [0]
        for a in nums:
            self.prefix.append(a + self.prefix[-1])


    def sumRange(self, i: int, j: int):
        return self.prefix[j+1] - self.prefix[i]

