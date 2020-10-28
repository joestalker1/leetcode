import bisect


class ExamRoom(object):
    def __init__(self, N):
        self.n = N
        self.students = []

    def seat(self):
        if not self.students:
            self.students.append(0)
            return 0
        dist = self.students[0]
        # start from 0
        student = 0
        # go over existent students to find leftmost with max distance
        for i, s in enumerate(self.students):
            if i:
                prev = self.students[i - 1]
                d = (s - prev) // 2
                if d > dist:
                    dist = d
                    student = prev + d
        # if rightmost is free and may be max distance
        if self.n - 1 - self.students[-1] > dist:
            student = self.n - 1
        bisect.insort(self.students, student)
        return student

    def leave(self, p):
        self.students.remove(p)


sol = ExamRoom(10)
print(sol.seat())
print(sol.seat())
print(sol.seat())
print(sol.seat())
print(sol.leave(4))
print(sol.seat())
