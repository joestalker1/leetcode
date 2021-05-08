class Solution:
    def minOperations(self, boxes: str):
        res = [0] * len(boxes)
        #accumulate balls
        cnt = 0
        # work to move cnt balls to i-position
        ops = 0
        # go from the left to right
        for i in range(len(boxes)):
            res[i] += ops
            if boxes[i] == '1':
                cnt += 1
            ops += cnt
        ops = 0
        cnt = 0
        #go from right to the left
        for i in range(len(boxes)-1,-1,-1):
            res[i] += ops
            if boxes[i] == '1':
                cnt += 1
            ops += cnt
        return res
