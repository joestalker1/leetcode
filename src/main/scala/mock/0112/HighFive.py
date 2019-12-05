class Solution(object):
    def highFive(self, items):
        if not items:
            return []
        res = []
        items.sort(key=lambda x:[x[0], -x[1]])
        count = 0
        mark = 0
        id1 = items[0][0]
        for item in items:
             if item[0] != id1:
                res.append([id1, mark / count])
                id1 = item[0]
                mark = item[1]
                count = 1
             elif count < 5 and item[0] == id1:
                 mark += item[1]
                 count += 1
        res.append([id1, mark / count])
        return res


sol = Solution()
print(sol.highFive([[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]))
