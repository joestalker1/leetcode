class MyCalendar:

    def __init__(self):
        self.booked = []

    def book(self, start, end):
        for s,e in self.booked:
            if max(s, start) < min(e, end):
                return False
        self.booked.append([start, end])
        return True


cal = MyCalendar()
#["MyCalendar","book","book","book","book","book","book","book","book","book","book"]
#[[],[47,50],[33,41],[39,45],[33,42],[25,32],[26,35],[19,25],[3,8],[8,13],[18,27]]
#[null,true,true,false, false,true,false,true,true,true,false]
print(cal.book(47,50))#true
print(cal.book(33,41))#true
print(cal.book(39,45))#false
print(cal.book(33,42))#false
print(cal.book(25,32))#true
print(cal.book(26,35))#false
print(cal.book(19,25))#true
print(cal.book(3,8))#true
print(cal.book(8,13))#true
print(cal.book(18,27))#false

#["MyCalendar","book","book","book"]
#[[],[10,20],[15,25],[20,30]]
# print(cal.book(10,20))#true
# print(cal.book(15,25))#false
# print(cal.book(20,30))#true



