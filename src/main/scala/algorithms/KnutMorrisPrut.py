def build_lps(s):
    lps = [0] * len(s)
    len_s = 0
    i = 1
    while i < len(s):
        if s[i] == s[len_s]:
            len_s += 1
            lps[i] = len_s
            i += 1
        else:
            if len_s != 0:
                len_s = lps[len_s-1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp(s,pat):
    lps = build_lps(pat)
    i = 0
    j = 0
    while i < len(s):
        if s[i] == s[j]:
            i += 1
            j += 1
        if j == len(pat):
            print('Found substring {} at {}'.format(s[i-j:i-j+len(pat)],i-j))
            j = lps[j-1]
        elif i < len(s) and s[i] != pat[j]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1

kmp('aaaaa', 'aa')
