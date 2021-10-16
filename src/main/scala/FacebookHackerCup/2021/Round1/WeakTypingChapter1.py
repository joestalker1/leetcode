def calc_switch_times_for_one_string(w):
    if len(w) <= 1:
        return 0
    lh = ['F', 'X']
    rh = ['F','O']
    hand = None
    times = 0
    i = 0
    while i < len(w):
        if w[i] == 'X':
            hand = lh
            break
        elif w[i] == 'O':
            hand = rh
            break
        i += 1

    while i < len(w):
        if w[i] not in hand:
            hand = lh
            if w[i] in rh:
                hand = rh
            times += 1
        i += 1
    return times

def input_data(fn):
    with open(fn, 'r') as rd:
        t = rd.readline()
        t = t.strip()
        t = int(t)
        for i in range(1, t+1):
            n = rd.readline()
            n = int(n.strip())
            s = []
            while n > 0:
                w = rd.readline().strip()
                s.append(w)
                n -= len(w)
            w = ''.join(s)
            switches = calc_switch_times_for_one_string(w)
            print('Case #{}: {}'.format(i, switches))

input_data('/Users/denis/Downloads/weak_typing_chapter_1_input (1).txt')
print
