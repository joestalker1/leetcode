from collections import Counter

t = int(input())
vowels = {'A', 'E', 'I', 'O','U'}


for i in range(t):
    s = input()
    s = s.strip()
    freq = Counter(s)
    cons_set = set()
    vow_set = set()
    cons_num = 0
    vow_num = 0
    for ch in s:
        if ch in vowels:
            vow_set.add(ch)
            vow_num += 1
        else:
            cons_num += 1
            cons_set.add(ch)
    vow_card = len(vow_set)
    cons_card = len(cons_set)
    if vow_card == 1 and cons_card == 1:
        ch1 = list(vow_set)[0]
        ch2 = list(cons_set)[0]
        print('Case #{}: {}'.format(i + 1, len(s) - max(freq[ch1],freq[ch2])))
    elif vow_card == 1:
        ch = list(vow_set)[0]
        print('Case #{}: {}'.format(i + 1, len(s) - freq[ch]))
    elif cons_card == 1:
        ch = list(cons_set)[0]
        print('Case #{}: {}'.format(i + 1, len(s) - freq[ch]))
    elif vow_card == 0 or cons_card == 0:
        print('Case #{}: {}'.format(i + 1, len(s)))
    else:
        # find frequent consonent and vowels
        max_cons = None
        for ch in freq:
            if ch in vowels:
                continue
            if max_cons is None or freq[max_cons] < freq[ch]:
                max_cons = ch
        max_vow = None
        for ch in freq:
            if ch in vowels:
                if max_vow is None or freq[max_vow] < freq[ch]:
                    max_vow = ch

        cost = min((cons_num-freq[max_cons]) * 2 + vow_num, (vow_num - freq[max_vow]) * 2 + cons_num)
        print('Case #{}: {}'.format(i + 1, cost))
    print
