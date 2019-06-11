class Solution:
    def does_cross(self, interval1, interval2):
        return interval2[0] <= interval1[0] <= interval2[1] or interval1[0] <= interval2[0] <= interval1[1]

    def merge(self, A, B, i, j, res):
        k = j
        while k < len(B) and self.does_cross(A[i], B[k]):
            left = max(A[i][0], B[k][0])
            right = min(A[i][1], B[k][1])
            res.append([left, right])
            k += 1

    def intervalIntersection(self, A, B):
        if not A or not B:
            return []

        #merge res1 and res2
        res = []
        i = 0
        j = 0
        while i < len(A) and j < len(B):
            if A[i][0] == B[j][0]:
                self.merge(A, B, i, j, res)
                i += 1
                self.merge(B, A, j, i, res)
                j += 1
            elif A[i][0] < B[j][0]:
                self.merge(A, B, i, j, res)
                i += 1
            else:
                self.merge(B, A, j, i, res)
                j += 1

        return res





sol = Solution()
print(sol.intervalIntersection([[3,7],[8,11],[13,18],[29,32],[33,35],[36,39],[41,45],[47,52],[56,74],[85,97]],
                               [[5,6],[8,12],[17,18],[19,26],[28,30],[31,32],[42,63],[64,65],[74,79],[96,98]]))
                               # [[3,7],[8,11],[13,18],[29,32],[33,35],[36,39],[41,45],[47,52],[56,74],[85,97]]))
# [[5,6],[8,11],[17,18],[29,30],[31,32],[42,45],[47,52],[56,63],[64,65],[74,74],[96,97]]

#print(sol.intervalIntersection([[3,5],[9,20]], [[4,5],[7,10],[11,12],[14,15],[16,20]]))
#print(sol.intervalIntersection([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]))