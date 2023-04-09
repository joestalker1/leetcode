import math

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        if not customers:
            return 0
        n = len(customers)
        min_penalty = math.inf
        closed_at = 0
        no_customer = [0] * len(customers)
        customer_come = [0] * len(customers)
        for i in range(len(customers)):
            no_customer[i] = no_customer[i - 1] if i > 0 else 0
            if customers[i] == 'N':
                no_customer[i] += 1
        for i in range(len(customers) - 1, -1, -1):
            customer_come[i] = customer_come[i + 1] if i < (n - 1) else 0
            if customers[i] == 'Y':
                customer_come[i] += 1

        for h in range(len(customers)):
            if h > 0:
                cur_penalty = no_customer[h-1] + customer_come[h]
            else:
                cur_penalty = customer_come[h]
            if cur_penalty < min_penalty:
                min_penalty = cur_penalty
                closed_at = h
        if no_customer[-1] < min_penalty:
            closed_at = n
        return closed_at


sol = Solution()
print(sol.bestClosingTime("YYNY"))#2