from collections import defaultdict
import heapq

class NumberContainers:

    def __init__(self):
        self.num_to_pos = defaultdict(list)
        self.index_to_num = {}

    def change(self, index: int, number: int) -> None:
        if index not in self.index_to_num:
            self.index_to_num[index] = number
            heapq.heappush(self.num_to_pos[number], index)
            return
        self.index_to_num[index] = number
        heapq.heappush(self.num_to_pos[number], index)

    def find(self, number: int) -> int:
        while self.num_to_pos[number] and self.index_to_num[self.num_to_pos[number][0]] != number:
            heapq.heappop(self.num_to_pos[number])
        return self.num_to_pos[number][0] if self.num_to_pos[number] else -1