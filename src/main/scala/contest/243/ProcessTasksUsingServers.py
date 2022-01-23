rom heapq import heappush,heappop,heapify

class Solution:
    def assignTasks(self, servers, tasks):
        n = len(servers)
        m = len(tasks)
        busy = []
        aval = []
        for i,weight in enumerate(servers):
            aval.append((0,weight, i))
        heapify(aval)    
        ans = [0] * m
        #m is number of tasks
        for t in range(m):
            while busy and busy[0][0] <= t or not aval:
                #end time and server index
                time,w,i = heappop(busy)
                # if task end time is less than t, let ignore time by applying 0
                if time <= t:
                    heappush(aval,(0,servers[i],i))
                else:
                    #this time effects the time when next task finishes.
                    heappush(aval,(time,servers[i],i))
            time,w,i = heappop(aval)
            ans[t] = i
            heappush(busy, (max(time, t) + tasks[t],servers[i], i))
        return ans