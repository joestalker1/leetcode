class Range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def is_overlapped(self, range):
        return self.start <= range.start <= self.end or range.start <= self.start <= range.end

    def merge(self, range):
        self.start = min(self.start, range.start)
        self.end = max(self.end, range.end)

    def consec(self, range):
        return self.end + 1 == range.start or range.end + 1 == self.start


class Solution:
    def addBoldTag(self, s: str, dict):
        if not s:
            return None
        ranges = []

        for word in dict:
            i = s.find(word)
            if i == -1:
                continue
            while i != -1 and i < len(s):
                j = i + len(word) - 1
                ranges.append(Range(i, j))
                i = s.find(word, j + 1)
        ranges.sort(key=lambda x:x.start)

        #combine ranges if they are overlapped or consecative

        while True:
            if len(ranges) > 1:
                new_ranges = []
                i = 0
                while i < len(ranges):
                    if i + 1 < len(ranges) and (ranges[i].is_overlapped(ranges[i+1]) or ranges[i].consec(ranges[i+1])):
                        ranges[i].merge(ranges[i+1])
                        new_ranges.append(ranges[i])
                        i += 2
                    else:
                        new_ranges.append(ranges[i])
                        i += 1
                if len(new_ranges) == len(ranges):
                    ranges = new_ranges
                    break
                ranges = new_ranges
            else:
                break
        res = []
        pos_to_range = {ranges[i].start:ranges[i] for i in range(len(ranges))}
        i = 0
        while i < len(s):
            if i in pos_to_range:
                a,b = pos_to_range[i].start,pos_to_range[i].end
                res.append("<b>{}</b>".format(s[a:b+1]))
                i = b + 1
            else:
                res.append(s[i])
                i += 1
        return ''.join(res)

sol = Solution()
print(sol.addBoldTag(s = "abcxyz123", dict = ["abc","123"]))








