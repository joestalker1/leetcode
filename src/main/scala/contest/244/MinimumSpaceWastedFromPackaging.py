import bisect
import math

class Solution:
    def minWastedSpace(self, packages, boxes) -> int:
        max_box = -math.inf
        for box in boxes:
            box.sort()
            max_box = max(max_box, box[-1])
        packages.sort()
        max_pack = packages[-1]
        if max_box < max_pack:
            return -1
        min_waste = inf
        sump = sum(packages)
        for box in boxes:
            if box[-1] < max_pack:
                continue
            i = 0
            waste = 0
            for j in range(len(box)):
                if box[j] < packages[0]:
                    continue
                ni = bisect.bisect_right(packages, box[j])
                if ni == -1:
                    continue
                waste += (ni - i) * box[j]
                i = ni
                if i >= len(packages):
                    break
            min_waste = min(min_waste, waste-sump)
        return min_waste % (10 ** 9 + 7)
