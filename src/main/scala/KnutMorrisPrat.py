def get_lps(pat):
    arr = [0] * len(pat)
    i = 1
    l = 0
    while i < len(pat):
        if pat[l] == pat[i]:
            l += 1
            arr[i] = l
            i += 1
        else:
            if l != 0:
                l = arr[l - 1]
            else:
                i += 1
    return arr


def search(pat, text):
    lps = get_lps(pat)
    i = 0
    j = 0
    while i < len(text):
        if pat[j] == text[i]:
            i += 1
            j += 1
        if j == len(pat):
            print('find at {}'.format(i - j))
            j = lps[j - 1]
        elif i < len(text) and pat[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1


txt = "ABABDABACDABABCABAB"
pat = "ABABCABAB"
search(pat, txt)
