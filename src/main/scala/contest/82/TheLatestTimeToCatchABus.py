class Solution:
    def latestTimeCatchTheBus(self, buses, passengers, capacity: int):
        # assert self._latestTimeCatchTheBus([15,16,17,7,10,20,13,12],[18,15,11,17,12,13,14,10,19,16],2) == 9,'test9'
        # assert self._latestTimeCatchTheBus([7,12,15,11,14,13,5,4,2,8,9,19],[2,5,10,12,8,19,9,14,4,7,15,13],2) == 18, 'test8'
        # assert self._latestTimeCatchTheBus([20,30,10],[19,13,26,4,25,11,21],2)== 20, 'test3'
        # assert self._latestTimeCatchTheBus([2],[2], 1) == 1, 'test2'
        # assert self._latestTimeCatchTheBus([3],[2,3],2) == 1, 'test1'
        # assert self._latestTimeCatchTheBus([3],[2],2) == 3, 'test4'
        # assert self._latestTimeCatchTheBus([3],[2], 1) == 1,'test5'
        # assert self._latestTimeCatchTheBus([5],[2,3],10000) == 5, 'test6'
        # assert self._latestTimeCatchTheBus([5],[7,8],1) == 5,'test7'
        return self._latestTimeCatchTheBus(buses, passengers, capacity)

    def _latestTimeCatchTheBus(self, buses, passengers, capacity: int) -> int:
        if not buses or not passengers:
            return 0
        buses.sort()
        passengers.sort()
        uniq_time = set()
        for t in passengers:
            uniq_time.add(t)
        res = 0
        m = len(passengers)
        n = len(buses)
        q = 0
        for i in range(n):
            curbus = buses[i]
            cnt = 0
            while q < m and passengers[q] <= curbus and cnt < capacity:
                t = passengers[q] - 1
                if t not in uniq_time:
                    res = t
                q += 1
                cnt += 1
            if cnt < capacity:
                while curbus in uniq_time:
                    curbus -= 1
                res = max(res, curbus)
        return res

sol = Solution()
print(sol.latestTimeCatchTheBus([18,8,3,12,9,2,7,13,20,5],[13,10,8,4,12,14,18,19,5,2,30,34],1))#11
print(sol.latestTimeCatchTheBus([3],[2],1))#1
print(sol.latestTimeCatchTheBus([2],[2],1))#1
print(sol.latestTimeCatchTheBus([5],[7,8],1))#5
print(sol.latestTimeCatchTheBus([10,20],[2,17,18,19],2))#16
#print(sol.latestTimeCatchTheBus([3],[2],1))#1
print(sol.latestTimeCatchTheBus([5],[2,3],10000))#5