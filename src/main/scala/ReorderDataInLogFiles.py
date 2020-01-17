class Solution:
    def reorderLogFiles(self, logs):
        if not logs:
            return []
        buckets = [[], []]
        for log in logs:
            parts = log.split()
            if '0' <= parts[1][0] <= '9':
                buckets[1].append(log)
            else:
                buckets[0].append(log)
        def cmp(x):
            parts = x.split()
            return [' '.join(parts[1:]),parts[0]]

        buckets[0].sort(key=cmp)
        res = []
        for s in buckets[0]:
            res.append(s)
        for s in buckets[1]:
            res.append(s)
        return res


sol = Solution()
print(sol.reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))

