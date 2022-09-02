class Solution(object):
    def intervalIntersection(self, A, B):
        sorted_events = []

        i, j = 0, 0

        while i < 2 * len(A) and j < 2 * len(B):
            p1, q1 = int(i / 2), i % 2
            p2, q2 = int(j / 2), j % 2

            if A[p1][q1] < B[p2][q2]:
                sorted_events.append([A[p1][q1], q1, 1])
                i += 1
            elif A[p1][q1] > B[p2][q2]:
                sorted_events.append([B[p2][q2], q2, 2])
                j += 1
            else:
                if q1 == 0:
                    sorted_events.append([A[p1][q1], q1, 1])
                    i += 1
                else:
                    sorted_events.append([B[p2][q2], q2, 2])
                    j += 1

        while i < 2 * len(A):
            p1, q1 = int(i / 2), i % 2
            sorted_events.append([A[p1][q1], q1, 1])
            i += 1

        while j < 2 * len(B):
            p2, q2 = int(j / 2), j % 2
            sorted_events.append([B[p2][q2], q2, 2])
            j += 1

        g = set()
        start, end = -1, -1
        out = []

        for i in range(len(sorted_events)):
            if sorted_events[i][1] == 0:
                g.add(sorted_events[i][2])
                if len(g) == 2:
                    start = sorted_events[i][0]
            else:
                g.remove(sorted_events[i][2])
                if len(g) == 1:
                    end = sorted_events[i][0]
                    out.append([start, end])

        return out


sol = Solution()
print(sol.intervalIntersection([[0,2],[5,10],[13,23],[24,25]],[[1,5],[8,12],[15,24],[25,26]]))