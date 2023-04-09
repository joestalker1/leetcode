import math

class Solution:
    def repairCars(self, ranks, cars):
        # assert self._repairCars([2], 1) == 2, 'test1'
        # assert self._repairCars([5,1], 2) == 6, 'test2'
        # assert self._repairCars([4,2,3,1], 10) == 16, 'test2'
        # assert self._repairCars([5,1,8], 6) == 16, 'test4'
        return self._repairCars(ranks, cars)

    def _repairCars(self, ranks, cars: int) -> int:
        if len(ranks) == 1:
            return cars * cars * ranks[0]

        def count_repair(min_time):
            # find mechanic takes min time
            fixed_cars = 0
            for i in range(len(ranks)):
                fixed_cars += int(math.sqrt(min_time // ranks[i]))
            return fixed_cars

        lo = 1
        hi = cars * cars * ranks[-1]
        while lo < hi:
            min_time = lo + (hi - lo) // 2
            fixed_cars = count_repair(min_time)
            if fixed_cars < cars:
                lo = min_time + 1
            else:
                hi = min_time
        return lo

