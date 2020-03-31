class Solution:
    def getPairs(self, a, b, target):
        if not a or not b:
            return []
        a.sort(key=lambda x: x[1])
        b.sort(key=lambda x: x[1])

        def find(a, b, target, res):
            p1 = 0
            p2 = len(b) - 1
            while p1 < p2:
                d = a[p1][1] + b[p2][1]
                if d == target:
                    while res and res[-1][2] > 0:
                        res.pop()
                    res.append([a[p1][0], b[p2][0], 0])
                elif d > target:
                    p2 -= 1
                else:
                    while res and res[-1][2] > d:
                        res.pop()
                    res.append([a[p1][0], b[p2][0], target - d])
                    p1 += 1

        res1 = []
        find(a, b, target, res1)
        res2 = []
        find(b, a, target, res2)
        res2 = [[x[1], x[0]] for x in res2]
        return [[x[0], x[1]] for x in res1 + res2]


sol = Solution()
# print(sol.getPairs(a=[[1, 2], [2, 4], [3, 6]],
#                    b=[[1, 2]],
#                    target=7))
print(sol.getPairs(a=[[1, 3], [2, 5], [3, 7], [4, 10]],
                   b=[[1, 2], [2, 3], [3, 4], [4, 5]],
                   target=10))
