from collections import defaultdict


def smallest(s1, chars):
    assert chars != ''
    # char frequency
    d = defaultdict(int)
    nneg = [0]  # number of negative entries in d

    def incr(c):
        d[c] += 1
        if d[c] == 0:
            # perhaps char with min frequencies are char set
            nneg[0] -= 1

    def decr(c):
        if d[c] == 0:
            nneg[0] += 1
        d[c] -= 1
    # decrease frequence for every char is from char set.
    # so this chars would have least frequencies
    for c in chars:
        decr(c)
    minlen = len(s1) + 1
    j = 0
    for i in range(len(s1)):
        # go to the right until meet all chars from char set
        while nneg[0] > 0:
            if j >= len(s1):
                return minlen
            incr(s1[j])
            j += 1
        # calculate min substring containing all char set
        minlen = min(minlen, j - i)
        # decrease leftmost char
        decr(s1[i])
    return minlen

print(smallest("figehaeci",  {'a', 'e', 'i'}))
