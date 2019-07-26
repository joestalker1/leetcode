class LogInfo:
    def __init__(self, id, day, month, hour, minutes, sec):
        self.day = day
        self.id = id
        self.month = month
        self.hour = hour
        self.minutes = minutes
        self.sec = sec

class LogSystem:
    def __init__(self):
        self.years = {}

    def put(self, id, timestamp):
        parts = timestamp.split(':')
        year = parts[0]
        month = self.con(parts, 1)
        day = self.con(parts, 2)
        hour = self.con(parts, 3)
        minutes = self.con(parts, 4)
        sec = self.con(parts, 5)
        log_info = LogInfo(id, day, month, hour, minutes, sec)
        if year not in self.years:
            self.years[year] = []
        self.years[year].append(log_info)

    def con(self, parts, i):
        s = ''
        for j in range(0, i + 1):
            s += parts[j]
        return s

    def retrieve(self, s, e, gra):
        parts1 = s.split(':')
        parts2 = e.split(':')
        year1 = self.con(parts1, 0)
        day1 = self.con(parts1, 2)
        month1 = self.con(parts1, 1)
        hour1 = self.con(parts1, 3)
        min1 = self.con(parts1, 4)
        sec1 = self.con(parts1, 5)
        day2 = self.con(parts2, 2)
        month2 = self.con(parts2, 1)
        year2 = self.con(parts2, 0)
        hour2 = self.con(parts2, 3)
        min2 = self.con(parts2, 4)
        sec2 = self.con(parts2, 5)
        by_year = []
        for y in range(int(year1), int(year2) + 1):
            s = str(y)
            if s in self.years:
                for li in self.years[s]:
                    by_year.append(li)
        if gra == 'Year':
            return list(map(lambda x: x.id, by_year))

        by_day = []
        for i in range(len(by_year)):
            if month1 <= by_year[i].month <= month2 and day1 <= by_year[i].day <= day2:
                by_day.append(by_year[i])
        if gra == 'Day':
            return list(map(lambda x: x.id, by_day))

        by_hour = []
        for i in range(len(by_day)):
            if hour1 <= by_day[i].hour <= hour2:
                by_hour.append(by_day[i])

        if gra == 'Hour':
            return list(map(lambda x: x.id, by_hour))

        by_min = []
        for i in range(len(by_hour)):
            if min1 <= by_hour[i].minutes <= min2:
                by_min.append(by_hour[i])

        if gra == 'Minute':
            return list(map(lambda x: x.id, by_min))

        by_sec = []
        for i in range(len(by_min)):
            if sec1 <= by_min[i].sec <= sec2:
                by_sec.append(by_min[i])
        return list(map(lambda x: x.id, by_sec))



sol = LogSystem()
#sol.put(1, "2017:01:01:23:59:59")
#sol.put(2, "2017:01:01:22:59:59")
#sol.put(3, "2016:01:01:00:00:00")
#print(sol.retrieve("2016:01:01:01:01:01","2017:01:01:23:00:00","Hour"))
#print(sol.retrieve("2016:01:01:01:01:01","2017:01:01:23:00:00","Year"))

sol.put(1, "2017:01:01:23:59:59")
sol.put(2, "2017:01:02:23:59:59")
print(sol.retrieve("2017:01:01:23:59:58","2017:01:02:23:59:58","Second"))

#["LogSystem","put","put","retrieve"]
#[[],[1,"2017:01:01:23:59:59"],[2,"2017:01:02:23:59:59"],["2017:01:01:23:59:58","2017:01:02:23:59:58","Second"]]

# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(s,e,gra)