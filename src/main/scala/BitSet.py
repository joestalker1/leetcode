class Bitset:

    def __init__(self, size: int):
        self.bits = [0] * size
        self.ones = 0

    def fix(self, idx: int) -> None:
        self.bits[idx] = 1
        self.ones += 1

    def unfix(self, idx: int) -> None:
        self.bits[idx] = 0
        self.ones -= 1

    def flip(self) -> None:
        self.ones = 0
        for i in range(len(self.bits)):
            self.bits[i] = 1 - self.bits[i]
            if self.bits[i] == 1:
                self.ones += 1

    def all(self) -> bool:
        return self.ones == len(self.bits)

    def one(self) -> bool:
        return self.ones > 0

    def count(self) -> int:
        return self.ones

    def toString(self) -> str:
        s = [str(self.bits[i]) for i in range(len(self.bits))]
        return ''.join(s)

