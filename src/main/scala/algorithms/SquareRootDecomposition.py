import math


class Solution:
    def __init__(self, input):
        self.vals = [0] * len(input)
        n = len(input)
        self.block_size = math.ceil(math.sqrt(n))
        self.blocks = [0] * self.block_size
        block_index = -1
        for i in range(n):
            self.vals[i] = input[i]
            if i % self.block_size == 0:
                block_index += 1
            self.blocks[block_index] += input[i]

    def update(self, i, value):
        blk = i // self.block_size
        self.blocks[blk] += value - self.vals[i]
        self.vals[i] = value

    def query(self, left, right):
        cur_sum = 0
        while left < right and left % self.block_size != 0 and left != 0:
            cur_sum += self.vals[left]
            left += 1
        while left + self.block_size - 1 <= right:
            cur_sum += self.blocks[left // self.block_size]
            left += self.block_size
        while left <= right:
            cur_sum += self.vals[left]
            left += 1
        return cur_sum


sol = Solution([3, 2, 4, 5, 1, 1, 5, 3, 7])
print(sol.query(0, 2))
sol.update(1, 6)
print(sol.query(0, 2))

