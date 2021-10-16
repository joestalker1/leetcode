from collections import defaultdict


def calc_happiness(attractions, n, k):
    cur_attractions = set()
    max_happiness = 0
    best_attractions = set()
    start = defaultdict(list)
    end = defaultdict(list)
    for i in range(len(attractions)):
        _,s,e = attractions[i]
        start[s].append(i)
        end[e + 1].append(i)
    cur_happiness = 0

    for d in range(1, n + 1):#days
        if d in start:
            # add new attraction
            for j in start[d]:
                cur_attractions.add(j)
                cur_happiness += attractions[j][0]
        if d in end:
            for j in end[d]:
                cur_attractions.discard(j)
                cur_happiness -= attractions[j][0]
        if cur_happiness > max_happiness:
            best_attractions = list(cur_attractions)
            max_happiness = cur_happiness
    best_attractions = list(best_attractions)
    best_attractions.sort(key=lambda x:-attractions[x][0])
    cur_happiness = 0
    for j in best_attractions[:k]:
        cur_happiness += attractions[j][0]
    return cur_happiness



def input_data():
    t = int(input())
    for i in range(1, t + 1):
        s = input()
        s = s.strip()
        arr = s.split(' ')
        d = int(arr[0])
        n = int(arr[1])
        k = int(arr[2])
        attractions = []
        for _ in range(n):
            s = input()
            s = s.strip()
            arr = s.split(' ')
            h = int(arr[0])
            s = int(arr[1])
            e = int(arr[2])
            attractions.append([h, s, e])
        happiness = calc_happiness(attractions, d, k)
        print('Case #{}: {}'.format(i, happiness))


input_data()
