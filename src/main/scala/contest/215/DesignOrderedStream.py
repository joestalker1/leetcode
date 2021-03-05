class OrderedStream:

    def __init__(self, n: int):
        self.chunks = [None] * (n + 1)
        self.last = 0

    def insert(self, id: int, value: str):
        self.chunks[id] = value
        if id - self.last == 1:
            n = len(self.chunks)
            res = []
            j = id
            while j < n and self.chunks[j]:
                res.append(self.chunks[j])
                j += 1
            self.last = j - 1
            return res
        return []



