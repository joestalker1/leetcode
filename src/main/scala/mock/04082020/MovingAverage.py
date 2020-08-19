class MovingAverage:

    def __init__(self, size: int):
        self.window_size = size
        self.nums = []

    def next(self, val: int) -> float:
        if len(self.nums) == self.window_size:
            self.nums.pop(0)
        self.nums.append(val)
        return sum(self.nums) // len(self.nums) if self.nums else 0

