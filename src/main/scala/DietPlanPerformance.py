class Solution:
    def calc_points(self, total, lower, upper):
        if total < lower:
            return -1
        if total > upper:
            return 1
        return 0

    def dietPlanPerformance(self, calories, k, lower, upper):
        if not calories or k < 0:
            return 0
        sum_of_k_days = sum(calories[:k])
        gain = self.calc_points(sum_of_k_days, lower, upper)
        i = 1
        while i <= len(calories) - k:
            sum_of_k_days -= calories[i - 1]
            sum_of_k_days += calories[i + k - 1]
            gain += self.calc_points(sum_of_k_days, lower, upper)
            i += 1
        return gain

sol = Solution()
print(sol.dietPlanPerformance(calories = [3,2], k = 2, lower = 0, upper = 1))
#print(sol.dietPlanPerformance([1,2,3,4,5], 1, 3, 3))
print(sol.dietPlanPerformance(calories = [6,5,0,0], k = 2, lower = 1, upper = 5))



