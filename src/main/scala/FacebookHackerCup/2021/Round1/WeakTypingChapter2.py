MOD = 10 ** 9 + 7

######## for test
def calc_for_all_subseq(w):
    if len(w) <= 1:
        return 0
    times = 0
    for l in range(2, len(w)+1):
        for i in range(len(w) - l + 1):
            j = i + l
            sub = w[i:j]
            t = calc_switch_times_for_one_string(sub)
            times += t
    return times


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
##########################################
def calc_switch_times(w):
    if len(w) <= 1:
        return 0
    n = len(w)
    dp = [0] * n
    left = [-1] * n
    if w[0] != 'F':
        left[0] = 0
    for i in range(1, n):
        if w[i] != 'F':
            left[i] = i
        else:
            left[i] = left[i-1]

    for i in range(1, n):
        if w[i] != 'F' and left[i-1] >= 0 and w[i] != w[left[i-1]]:
            dp[i] = (dp[i-1] + left[i - 1] + 1) % MOD
        else:
            dp[i] = dp[i-1]
    return sum(dp) % MOD

def run_tests():
    #assert calc_switch_times('FOX') == calc_for_all_subseq('FOX'), 'test0'
    assert calc_switch_times('XXOO') == calc_for_all_subseq('XXOO'), 'test1'
    assert calc_switch_times('XXOXO') == calc_for_all_subseq('XXOXO'), 'test2'
    assert calc_switch_times('FXXFXFOOXF') == calc_for_all_subseq('FXXFXFOOXF'), 'test3'
    assert calc_switch_times('XFOFXFOFXFOFX') == calc_for_all_subseq('XFOFXFOFXFOFX'), 'test4'

def run_main(fn, calc_times):
    with open(fn, 'r') as rd:
        t = rd.readline()
        t = t.strip()
        t = int(t)
        for i in range(1, t + 1):
            n = rd.readline()
            n = int(n.strip())
            s = []
            while n > 0:
                w = rd.readline().strip()
                s.append(w)
                n -= len(w)
            w = ''.join(s)
            switches = calc_times(w)
            print('Case #{}: {}'.format(i, switches))

#run_tests()
#run_main('/Users/denis/Downloads/weak_typing_chapter_2_validation_input (2).txt', calc_for_all_subseq)
run_main('/Users/denis/Downloads/weak_typing_chapter_2_input (1).txt', calc_switch_times)
#print(calc_for_all_subseq('XFOFX'))#4
#print(calc_switch_times('FOX'))
print

