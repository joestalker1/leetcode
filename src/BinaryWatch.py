class Solution:
    def __init__(self):
        self.hours = [1, 2, 4, 8]
        self.minutes = [1, 2, 4, 8, 16, 32]

    def read_binary_watch(self, res, time, num,start_point):
        if num == 0:
            h = time[0]
            m = time[1]
            res.append('%d:%02d' % (h, m))
            return
        for i in range(start_point, len(self.hours) + len(self.minutes)):
            if i < len(self.hours):
                time[0] += self.hours[i]
                if time[0] < 12:
                    self.read_binary_watch(res, time, num - 1,i + 1)
                time[0] -= self.hours[i]
            else:
                time[1] += self.minutes[i- len(self.hours)]
                if time[1] < 60:
                    self.read_binary_watch(res, time, num - 1, i + 1)
                time[1] -= self.minutes[i - len(self.hours)]

    def readBinaryWatch(self, num):
        res = []
        self.read_binary_watch(res, [0,0], num, 0)
        return sorted(res)


sol = Solution()
print(sol.readBinaryWatch(2))

