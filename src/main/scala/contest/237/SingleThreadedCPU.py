from heapq import heappop,heappush

class Solution:
    def getOrder(self, tasks):
        sorted_tasks = [[i, tasks[i][0], tasks[i][1]] for i in range(len(tasks))]
        sorted_tasks.sort(key=lambda x: x[1])
        next_task = []
        res = []
        time = 0
        i = 0
        while len(res) < len(tasks):
            #put new task
            while i < len(tasks) and sorted_tasks[i][1] <= time:
                heappush(next_task, (sorted_tasks[i][2], sorted_tasks[i][0]))
                i += 1
            if not next_task:
                time = sorted_tasks[0][1]
                continue
            _,j = heappop(next_task)
            res.append(j)
            time += tasks[j][1]
        return res


res = Solution()
print(res.getOrder([[19,13],[16,9],[21,10],[32,25],[37,4],[49,24],[2,15],[38,41],[37,34],[33,6],[45,4],[18,18],[46,39],[12,24]]))
print(res.getOrder([[7,10],[7,12],[7,5],[7,4],[7,2]]))
print(res.getOrder([[1,2],[2,4],[3,2],[4,1]]))








