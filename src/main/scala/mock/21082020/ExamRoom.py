from bisect import bisect_left


class ExamRoom:

    def __init__(self, N):
        self.n = N
        self.seats = []

    def seat(self):
        if not self.seats:
            self.seats.append(0)
            return 0

        def can_go(x):
            if not self.seats:
                return True
            i = bisect_left(self.seats, x)
            left_dist = self.n - 1
            right_dist = self.n - 1
            if i - 1 >= 0:
                left_dist = abs(self.seats[i - 1] - x)
            if i < len(self.seats):
                right_dist = abs(self.seats[i] - x)
            if left_dist < right_dist:
                return True
            return False
        a = 1
        while (a * 2) < self.n and can_go(a*2):
            a *= 2
        a = a // 2
        if a >= self.n:
            self.seats.append(self.n-1)
            return self.n-1
        else:
            i = bisect_left(self.seats, a)
            self.seats.insert(i, a)
            return a


    def leave(self, p: int):
        i = bisect_left(self.seats, p)
        self.seats.pop(i)


er = ExamRoom(10)
print(er.seat())
print(er.seat())
print(er.seat())
print(er.seat())
er.leave(4)
print(er.seat())
