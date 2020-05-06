class Solution:
    def balance(self, requests):
        if not requests or len(requests) < 5:
            return False
        left_sum = requests[0]
        left = 1
        right = len(requests) - 2
        right_sum = requests[-1]
        total_sum = sum(requests)

        while left < right:
            mid_sum = total_sum - left_sum - right_sum - requests[left] - requests[right]
            if mid_sum < left_sum or mid_sum < right_sum:
                return False
            if mid_sum == right_sum == left_sum:
                return True

            if left_sum <= right_sum:
                left_sum += requests[left]
                left += 1
            else:
                right_sum += requests[right]
                right -= 1
        return False


sol = Solution()
print(sol.balance([1, 1, 1, 1, 1, 1]))
print(sol.balance([1, 3, 4, 2, 2, 2, 1, 1, 2]))
