from collections import defaultdict

class Solution:
    def findingUsersActiveMinutes(self, logs, k):
        if not logs:
            return None
        count = defaultdict(set)
        for id,minutes in logs:
            count[id].add(minutes)
        count = {k:len(minutes) for k,minutes in count.items()}
        ans = [0] * (k + 1)
        for k,count_of_uniq_min in count.items():
            ans[count_of_uniq_min-1] += 1
        return ans

sol = Solution()
print(sol.findingUsersActiveMinutes([[0,5],[1,2],[0,2],[0,5],[1,3]], 5))