class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.pool = set([i for i in range(maxNumbers)])

    def get(self) -> int:
        return self.pool.pop() if self.pool else -1

    def check(self, number: int) -> bool:
        return number in self.pool

    def release(self, number: int) -> None:
        self.pool.add(number)

#["PhoneDirectory","release","get","release","release","get","get","check","get","release","get","release","release","get","check","release"]
#[[3],               [2],    [],[2],[0],[],[],[1],[],[0],[],[0],[0],[],[1],[1]]

pd = PhoneDirectory(3)

