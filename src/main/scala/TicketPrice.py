import heapq

from collections import defaultdict
from copy import copy

def get_itinerary(flights, source, destination, k):
    costs = defaultdict(lambda: float('inf'))
    costs[source] = 0

    prevs = {}

    for _ in range(k + 1):
        new_costs = copy(costs)

        for u, v, cost in flights:
            if costs[u] + cost < new_costs[v]:
                new_costs[v] = costs[u] + cost
                prevs[v] = u

        costs = new_costs

    if costs[destination] == float('inf'):
        return -1
    else:
        path = [destination]

        while path[-1] != source:
            path.append(prevs[path[-1]])
        path.reverse()

        return costs[destination], path


flights = [
    ('JFK', 'ATL', 150),
    ('ATL', 'SFO', 400),
    ('ORD', 'LAX', 200),
    ('LAX', 'DFW', 80),
    ('JFK', 'HKG', 800),
    ('ATL', 'ORD', 90),
    ('JFK', 'LAX', 500),
]
print(get_itinerary(flights, "JFK", "LAX", 3))