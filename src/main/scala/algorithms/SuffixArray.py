class Suffix:
    def __init__(self):
        self.rank = [0, 0]
        self.index = 0


class SuffixArray:
    def build(self, s):

        def cmp(a):
            return [a.rank[0],a.rank[1]]

        suffix = [0] * len(s)
        for i in range(len(suffix)):
            suffix[i] = Suffix()

        for i in range(len(suffix)):
            suffix[i].index = i
            suffix[i].rank[0] = ord(s[i]) - ord('a')
            suffix[i].rank[1] = -1
            if i + 1 < len(s):
                suffix[i].rank[1] = ord(s[i + 1]) - ord('a')

        suffix.sort(key=cmp)
        k = 4
        ind = [0] * len(s)
        while k < 2 * len(s):
            rank = 0
            prev_rank = suffix[0].rank[0]
            suffix[0].rank[0] = rank
            ind[suffix[0].index] = 0
            for i in range(1, len(s)):
                if suffix[i].rank[0] == prev_rank and suffix[i].rank[1] == suffix[i-1].rank[1]:
                    prev_rank = suffix[i].rank[0]
                    suffix[i].rank[0] = rank
                else:
                    prev_rank = suffix[i].rank[0]
                    rank += 1
                    suffix[i].rank[0] = rank
                ind[suffix[i].index] = i
            for i in range(len(s)):
                nextindex = suffix[i].index + k // 2
                suffix[i].rank[1] = -1
                if nextindex < len(s):
                    suffix[i].rank[1] = suffix[ind[nextindex]].rank[0]
            suffix.sort(key=cmp)
            k *= 2
        suffix_arr = [0] * len(s)
        for i in range(len(s)):
            suffix_arr[i] = suffix[i].index

        return suffix_arr


sol = SuffixArray()
print(sol.build("banana"))

