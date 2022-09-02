from collections import Counter

class DetectSquares:

    def __init__(self):
        self.freq = Counter()

    def add(self, point) -> None:
        self.freq[(point[0], point[1])] += 1

    def count(self, point) -> int:
        x1, y1 = point
        square_cnt = 0
        for (x3, y3), cnt3 in self.freq.items():
            if abs(x3 - x1) == 0 or abs(x3 - x1) != abs(y3 - y1):
                continue
            square_cnt += cnt3 * self.freq[(x3, y1)] * self.freq[(x1, y3)]
        return square_cnt

