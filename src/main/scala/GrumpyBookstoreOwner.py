class Solution:
    def maxSatisfied(self, customers, grumpy, X):
        win = 0
        max_satisfied = 0
        satisfied = 0
        for i,x in enumerate(customers):
            if grumpy[i] == 0:
                satisfied += customers[i]
            else:
                win += customers[i]
            if i >= X:
                win -= grumpy[i - X] * customers[i - X]
            max_satisfied = max(max_satisfied, win)
        return satisfied + max_satisfied


sol = Solution()
print(sol.maxSatisfied([1], [0], 1))  # 1
print(sol.maxSatisfied([4, 10, 10], [1, 1, 0], 2))#24
print(sol.maxSatisfied(customers=[1, 0, 1, 2, 1, 1, 7, 5], grumpy=[0, 1, 0, 1, 0, 1, 0, 1], X=3))#16
