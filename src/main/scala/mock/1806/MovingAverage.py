class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.nums = []

    def next(self, val: int) -> float:
        if self.size == len(self.nums):
            self.nums.pop(0)
        self.nums.append(val)
        return sum(self.nums) // self.size


sol = MovingAverage(3)
print(sol.next(1))
print(sol.next(10))
print(sol.next(3))
print(sol.next(5))




