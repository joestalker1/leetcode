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

def kasai(txt, suffix_arr):
    lcp = [0] * len(txt)
    inv_suff = [0] * len(txt)

    for i in range(len(suffix_arr)):
        inv_suff[suffix_arr[i]] = i

    k = 0
    for i in range(len(suffix_arr)):
        if inv_suff[i] == len(suffix_arr) - 1:
            k = 0
            continue
        j = suffix_arr[inv_suff[i] + 1]
        while i + k < len(suffix_arr) and j + k < len(suffix_arr) and txt[i + k] == txt[j + k]:
            k += 1
        lcp[inv_suff[i]] = k
        if k > 0:
            k -= 1
    return lcp

def count_distinct_substring(txt):
    suffix_arr = SuffixArray().build(txt)
    lcp = kasai(txt, suffix_arr)
    res = len(txt) - suffix_arr[0]
    for i in range(1, len(lcp)):
        res += len(txt) - suffix_arr[i] - lcp[i - 1]
    res += 1
    return res

n = int(input())
arr = []
for i in range(n):
    s = input()
    arr.append(s)

for s in arr:
    if len(s) == 0:
        print(0)
    else:
        distinct_str = count_distinct_substring(s)
        print(distinct_str)
