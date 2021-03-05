from math import inf

class Solution:
    def minimumTimeRequired(self, jobs, k):
        max_min_sum = inf
        jobs.sort(reverse=True)
        workload = [0] * k

        def dfs(cur):
            nonlocal max_min_sum
            if cur == len(jobs):
                max_min_sum = min(max_min_sum, max(workload))
                return
            seen = set()
            for j in range(k):
                if workload[j] in seen or workload[j] + jobs[cur] >= max_min_sum:
                    continue
                #prevent to consider another same wokrloads
                seen.add(workload[j])
                workload[j] += jobs[cur]
                dfs(cur + 1)
                #seen.discard(workload[j])
                workload[j] -= jobs[cur]
        dfs(0)
        return max_min_sum


sol = Solution()
print(sol.minimumTimeRequired([12,13,14,17,25], 3))#29
print(sol.minimumTimeRequired([3,2,3],3))#3
print(sol.minimumTimeRequired([1,2,4,7,8],2))#11









