class NumArray:

    def __init__(self, nums):
        #store sums
        self.tree = [0] * (len(nums) + 1)
        #store values
        self.nums = nums
        for i in range(len(nums)):
            self.init(i, nums[i])

    def init(self, index: int, val: int) -> None:
        index += 1
        while index < len(self.tree):
            self.tree[index] += val
            index += index & (-index)

    def update(self, index, val):
        diff = val - self.nums[index]
        #set up new value
        self.nums[index] = val
        #update every values by diff
        self.init(index, diff)

    def sum(self, index):
        cur_sum = 0
        index += 1
        while index > 0:
            cur_sum += self.tree[index]
            index -= index & (-index)
        return cur_sum

    def sumRange(self, left: int, right: int) -> int:
        if left > right:
            return 0
        return self.sum(right) - self.sum(left - 1)


sol = NumArray([1,3,5])
#["NumArray","sumRange","update","sumRange"]
#[[[1,3,5]],[0,2],[1,2],[0,2]]
print(sol.sumRange(0,2))#9
sol.update(1,2)
print(sol.sumRange(0,2))# 8



