class MyCalendarTwo:

    def __init__(self):
        self.cal = []
        self.overlaps = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.overlaps:
            if start < e and end > s:
                return False
        for s, e in self.cal:
            if start < e and end > s:
                # store overlapped interval
                self.overlaps.append([max(s, start), min(e, end)])
        self.cal.append([start, end])
        return True


cal = MyCalendarTwo()
print(cal.book(10, 20))  # true
print(cal.book(50, 60))  # true
print(cal.book(10, 40))  # true
print(cal.book(5, 15))  # false
print(cal.book(5, 10))  # true
print(cal.book(25, 55))  # true
