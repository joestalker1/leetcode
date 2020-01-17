from collections import defaultdict

class Solution:
    def numBusesToDestination(self, routes, S, T):
        if not routes:
            return -1
        stop_to_bus = defaultdict(set)
        g = defaultdict(list)
        for bus,route in enumerate(routes):
             for bs in route:
                if bus not in stop_to_bus[bs]:
                    for n in list(stop_to_bus[bs]):
                        g[n].append(bus)
                        g[bus].append(n)
                stop_to_bus[bs].add(bus)
        # set up 1 if we go by this bus but if S==T we don't ride by bus.
        q = [[b,1] for b in list(stop_to_bus[S])]
        seen = set(stop_to_bus[S])
        dest = stop_to_bus[T]
        while q:
            bus,count = q.pop(0)
            if bus in dest:
                if S == T:
                    return 0
                return count
            for nei in g[bus]:
                if nei not in seen:
                    seen.add(nei)
                    q.append([nei, count + 1])
        return -1


sol = Solution()
print(sol.numBusesToDestination([[1,7],[3,5]],5,5))
print(sol.numBusesToDestination([[25,33],[3,5,13,22,23,29,37,45,49],[15,16,41,47],[5,11,17,23,33],[10,11,12,29,30,39,45],[2,5,23,24,33],[1,2,9,19,20,21,23,32,34,44],[7,18,23,24],[1,2,7,27,36,44],[7,14,33]],7, 47))
print(sol.numBusesToDestination([[1, 2, 7], [3, 6, 7]], 1, 6))



