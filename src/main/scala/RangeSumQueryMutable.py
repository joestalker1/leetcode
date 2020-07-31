from collections import defaultdict

class NumArray:

    def __init__(self, nums):
        self.arr = nums
        self.prefix = [0]
        self.updates = defaultdict(int)
        self.update_count = 0
        for i in range(len(nums)):
            self.prefix.append(self.prefix[-1] + nums[i])


    def update(self, i: int, val: int) -> None:
        self.updates[i] = val
        self.update_count += 1
        # self.arr[i] = val
        # for j in range(i, len(self.arr)):
        #     self.prefix[j+1] += diff

    def sumRange(self, i, j):
        #apply the earlier persisted updates
        if self.update_count == 0:
            return self.prefix[j+1] - self.prefix[i]
        for i in range(self.updates):
            self.arr[i] = self.u


sol = NumArray([1,3,5])
#["NumArray","sumRange","update","sumRange"]
#[[[1,3,5]],[0,2],[1,2],[0,2]]
print(sol.sumRange(0,2))#9
sol.update(1,2)
print(sol.sumRange(0,2))# 8



