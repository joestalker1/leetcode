import heapq


class StockPrice:

    def __init__(self):
        self.min_price = []
        self.max_price = []
        self.last_timestamp = 0
        self.ts_to_price = {}

    def update(self, timestamp: int, price: int) -> None:
        self.ts_to_price[timestamp] = price

        if timestamp >= self.last_timestamp:
            self.last_timestamp = timestamp

        heapq.heappush(self.min_price, (price, timestamp))
        heapq.heappush(self.max_price, (-price, timestamp))

    def current(self) -> int:
        return self.ts_to_price[self.last_timestamp]

    def maximum(self) -> int:
        while self.max_price and -self.max_price[0][0] != self.ts_to_price[self.max_price[0][1]]:
            heapq.heappop(self.max_price)
        return -self.max_price[0][0]

    def minimum(self) -> int:
        while self.min_price and self.min_price[0][0] != self.ts_to_price[self.min_price[0][1]]:
            heapq.heappop(self.min_price)
        return self.min_price[0][0]


sol = StockPrice()
sol.update(1, 10)
sol.update(1, 10)
sol.update(2, 5)
print(sol.current())
print(sol.minimum())
print(sol.maximum())
sol.update(1,2)
print(sol.current())
print(sol.minimum())
print(sol.maximum())
