class Solution:
    def dietPlanPerformance(self, calories, k, lower, upper):
        if not calories or k <= 0:
            return 0
        points = 0
        sum_cal = 0
        stack = []
        for calory in calories:
            stack.append(calory)
            sum_cal += calory
            if len(stack) == k:
                if sum_cal < lower:
                    points -= 1
                elif sum_cal > upper:
                    points += 1
                cal = stack.pop(0)
                sum_cal -= cal
        return points


sol = Solution()
#print(sol.dietPlanPerformance(calories = [3,2], k = 2, lower = 0, upper = 1))
print(sol.dietPlanPerformance(calories = [6,5,0,0], k = 2, lower = 1, upper = 5))
print(sol.dietPlanPerformance(calories = [1,2,3,4,5], k = 1, lower = 3, upper = 3))


