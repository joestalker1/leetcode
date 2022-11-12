class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0] * k
        self.cur_size = 0
        self.front_pos = 0

    def enQueue(self, value: int) -> bool:
        if len(self.queue) == self.cur_size:
            return False
        self.queue[(self.front_pos + self.cur_size) % len(self.queue)] = value
        self.cur_size += 1
        return True

    def deQueue(self) -> bool:
        if self.cur_size == 0:
            return False
        self.front_pos = (self.front_pos + 1) % len(self.queue)
        self.cur_size -= 1
        return True

    def Front(self) -> int:
        if self.cur_size == 0:
            return -1
        return self.queue[self.front_pos]

    def Rear(self) -> int:
        if self.cur_size == 0:
            return -1
        return self.queue[(self.front_pos + self.cur_size - 1) % len(self.queue)]

    def isEmpty(self) -> bool:
        return self.cur_size == 0

    def isFull(self) -> bool:
        return len(self.queue) == self.cur_size