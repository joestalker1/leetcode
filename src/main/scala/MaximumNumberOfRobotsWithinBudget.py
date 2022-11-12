from sortedcontainers import SortedList

class Solution:
    def maximumRobots(self, chargeTimes, runningCosts, budget: int) -> int:
        if not chargeTimes or not runningCosts:
            return 0
        j = 0
        cur_run_time = 0
        max_charge_time = SortedList()
        for i in range(len(runningCosts)):
            cur_run_time += runningCosts[i]
            max_charge_time.add(chargeTimes[i])
            cur_cost = cur_run_time * (i - j + 1) + max_charge_time[-1]
            if cur_cost > budget:
                cur_run_time -= runningCosts[j]
                max_charge_time.remove(chargeTimes[j])
                j += 1
        return len(chargeTimes) - j