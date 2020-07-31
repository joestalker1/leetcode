class Solution(object):
    def kEmptySlots(self, bulbs, k):
        days = [0] * len(bulbs)
        for i in range(len(bulbs)):
            days[bulbs[i] - 1] = i + 1

        ans = float('inf')
        left, right = 0, k + 1
        while right < len(days):
            for i in range(left + 1, right):
                if days[i] < days[left] or days[i] < days[right]:
                    left, right = i, i + k + 1
                    break
            else:
                ans = min(ans, max(days[left], days[right]))
                left, right = right, right + k + 1

        return ans if ans < float('inf') else -1


sol = Solution()
print(sol.kEmptySlots([1, 3, 2], 1))
