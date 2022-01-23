class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # assert self._minInterval([[1,2],[1,3]], [1]) == [2],'test0'
        # assert self._minInterval([[1,2],[2,4]], [1]) == [2],'test1'
        # assert self._minInterval([[1,2]], [10]) == [-1],'test3'
        # assert self._minInterval([[1,6]],[1,2,3]) == [6,6,6],'test4'
        return self._minInterval(intervals, queries)

    def _minInterval(self, intervals, queries):
        if not intervals or not queries:
            return [-1]
        # sort intervals by start,end
        sorted_int = [[intervals[i][0], intervals[i][1]] for i in range(len(intervals))]
        sorted_int.sort()
        # sort queries
        sorted_queries = [q for q in queries]
        sorted_queries.sort()
        sort_inter_by_size = []
        i = 0
        q_to_sz = {}
        for q in sorted_queries:
            # add interval to queue if its start <= current q,add its size to get interval with min size
            while i < len(sorted_int) and sorted_int[i][0] <= q:
                l, r = sorted_int[i]
                heappush(sort_inter_by_size, [r - l + 1, r])
                i += 1
            # pop up intervals that don't include q
            while sort_inter_by_size and sort_inter_by_size[0][1] < q:
                heappop(sort_inter_by_size)
            # get first interval with min size from queue if it exists otherwise -1
            q_to_sz[q] = sort_inter_by_size[0][0] if sort_inter_by_size else -1
        return [q_to_sz[q] for q in queries]
    