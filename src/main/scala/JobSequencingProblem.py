import heapq

class Solution:

    # Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self, Jobs, n):
        if not Jobs or n == 0:
            return []
        sorted_job = [[Jobs[i][1],Jobs[i][2]] for i in range(n)]
        sorted_job.sort()
        job = []
        total_profit = 0
        job_cnt = 0
        for i in range(len(sorted_job)-1,-1,-1):
            if i == 0:
                aval_slots = sorted_job[i][0]
            else:
                aval_slots = sorted_job[i][0] - sorted_job[i-1][0]
            heapq.heappush(job, (-sorted_job[i][1],sorted_job[i][0]))
            while aval_slots and job:
                profit,_ = heapq.heappop(job)
                total_profit += -profit
                job_cnt += 1
                aval_slots -= 1
        return [job_cnt, total_profit]


sol = Solution()
print(sol.JobScheduling([(1,4,20),(2,1,10),(3,1,40),(4,1,30)],4))