def find_max(scores):
    j = 0
    max_score = 0
    for i in range(len(scores)):
        if max_score < scores[i]:
            max_score = scores[i]
            j = i
    return j if max_score != 0 else None

def max_score(scores):
    mural = 0
    j = find_max(scores)
    mural += 1

    while True:
        j = 0
        max_score = 0
        for i in range(len(scores)):
            if max_score < scores[i]:
                max_score = scores[i]
                j = i
        mural += max_score
        if max_score == 0:
            return mural
        if j == 0:
            k = len(scores) - 1
            while k >= 0 and scores[k] == 0:
                k -= 1
            if k < 0:
                return
            scores[k] = 0
        if j == len(scores) - 1:
            k = 0
            while k < len(scores) and scores[k] == 0:
                k += 1
            if k == len(scores):
                return
            scores[k] = 0
        if scores[j - 1] != 0:
            scores[j - 1] = 0
        elif scores[j + 1] != 0:
            scores[j + 1] = 0
    return mural


n = int(input())
for i in range(n):
    t = int(input())
    s = input()
    scores = list(map(lambda x: int(x), s))
    print(max_score(scores))
