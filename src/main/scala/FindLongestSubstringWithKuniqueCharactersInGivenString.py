from collections import defaultdict

def kUniques(s, k):
    uniq = defaultdict(int)
    j = 0
    res = [0, 0]
    for i in range(len(s)):
        uniq[s[i]] += 1
        if k == len(uniq):
            if res[1] - res[0] < i - j:
                res = [j, i]
        while len(uniq) > k and j <= i:
            uniq[s[j]] -= 1
            if uniq[s[j]] == 0:
                uniq.pop([s[j]])
            j += 1
            if k == len(uniq):
                if res[1] - res[0] < i - j:
                    res = [j, i]
    return s[res[0]:res[1] + 1]

print(kUniques("aabbcc",3))
