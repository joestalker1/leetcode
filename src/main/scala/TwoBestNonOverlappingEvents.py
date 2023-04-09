from sortedcontainers import SortedDict

class Solution:
    def maxTwoEvents(self, events) -> int:
        # assert self._maxTwoEvents([[1,3,2],[4,5,2],[2,4,3]]) == 4,'test1'
        # assert self._maxTwoEvents([[1,3,2],[4,5,2],[1,5,5]]) == 5,'test2'
        # assert self._maxTwoEvents([[1,5,3],[1,5,1],[6,6,5]]) == 8,'test3'
        return self._maxTwoEvents(events)

    def _maxTwoEvents(self, events) -> int:
        if len(events) < 1:
            return 0
        if len(events)< 2:
            return events[0][2]
        start_to_val= SortedDict()
        max_so_far = 0
        events.sort(key=lambda x:x[0])
        max_val = 0
        for i in range(len(events)-1,-1,-1):
            #key position
            j = start_to_val.bisect_right(events[i][1])
            max_so_far = max(max_so_far, events[i][2])
            if start_to_val and j < len(start_to_val):
                k = start_to_val.keys()[j]
                max_val = max(max_val,events[i][2] + start_to_val[k])
            else:
                max_val = max(max_val, max_so_far)
            start_to_val[events[i][0]] = max_so_far
        return max_val

        return find_max_sum(0,0)

