from collections import Counter,defaultdict
from math import inf

t = int(input())

def dfs(adj_lst,dist, node, target, cur_path):
    if node == target:
        return 0
    cost = inf
    for nei in adj_lst[node]:
        if dist[ord(nei) - ord('A')] > cur_path:
            dist[ord(nei) - ord('A')] = cur_path
            cost = min(cost,1 + dfs(adj_lst,dist, nei, target, cur_path + 1))
    return cost

for i in range(1, t + 1):
    s = input()
    s = s.strip()
    k = int(input())
    freq = Counter(s)
    freq_len = len(freq)
    if k == 0:
        if freq_len == 1:
            print('Case #{}: {}'.format(i, 0))
        else:
            print('Case #{}: {}'.format(i, -1))
    else:
        adj_lst = defaultdict(list)
        cand = set()
        for j in range(k):
            p = input()
            p = p.strip()
            adj_lst[p[0]].append(p[1])
            cand.add(p[1])
        if freq_len == 1:
            print('Case #{}: {}'.format(i, 0))
        else:
            cost = inf
            cand = list(cand)
            cand.sort(key=lambda x:-freq[x])
            for to_ch in cand:
                # try to convert the rest chars to ch
                trans_cost = 0
                for ch in s:
                    if ch == to_ch:
                        continue
                    dist = [inf] * 26
                    dist[ord(ch) - ord('A')] = 0
                    char_cost = dfs(adj_lst,dist, ch, to_ch, 0)
                    if char_cost == inf:
                        trans_cost = inf
                        break
                    trans_cost += char_cost
                cost = min(cost, trans_cost)
            cost = cost if cost != inf else -1
            print('Case #{}: {}'.format(i, cost))
    print
# Case #1: 2
# Case #2: -1
# Case #3: 0
# Case #4: 3
# Case #5: -1
# Case #6: 8
# Case #7: 100

# Case #1: 2
# Case #2: -1
# Case #3: 0
# Case #4: 3
# Case #5: -1
# Case #6: 8
# Case #7: 100
# Case #8: 5
# Case #9: 108
# Case #10: -1
# Case #11: 103



