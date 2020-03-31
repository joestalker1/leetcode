class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hits = [0] * 300
        self.seconds = [-1] * 300

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        i = (timestamp - 1) % 300
        if self.seconds[i] != timestamp:
            self.hits[i] = 1
            self.seconds[i] = timestamp
        else:
            self.hits[i] += 1

    def getHits(self, timestamp: int) -> int:
        res = 0
        min_t = max(0,timestamp - 300)
        max_t = timestamp
        for i in range(len(self.hits)):
            if min_t < self.seconds[i] <= max_t:
                res += self.hits[i]
        return res


counter = HitCounter()
counter.hit(1);


counter.hit(2);

#hit at timestamp 3.
counter.hit(3);

#get hits at timestamp 4, should return 3.
print(counter.getHits(4))

# hit at timestamp 300.
counter.hit(300);

# get hits at timestamp 300, should return 4.
print(counter.getHits(300))

# get hits at timestamp 301, should return 3.
print(counter.getHits(301))
