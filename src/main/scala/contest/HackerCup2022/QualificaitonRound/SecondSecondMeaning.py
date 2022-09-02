import math
import utils
import random
import itertools

class Trie:
    def __init__(self):
        self.bin = {}

    def add(self, s):
        p = self.bin
        for ch in s:
            if ch not in p:
                p[ch] = {}
            p = p[ch]

    def find_prefix(self, s):
        if not self.bin:
            return False
        p = self.bin
        for ch in s:
            if ch not in p:
                return False
            p = p[ch]
        return True


def gen_perm(chars, i):
    if i == len(chars):
        yiled chars[::]
    for j in range(i, len(chars)):
        chars[i],chars[j] = chars[j],chars[i]
        yield gen_perm(chars, i+1)
        chars[i], chars[j] = chars[j], chars[i]


def solve(buf):
    l = 0
    t = int(buf[l])
    l += 1
    res = []
    for k in range(1, t + 1):
        n = int(buf[l])
        l += 1
        c1 = buf[l].strip()
        l += 1
        res.append(f'Case #{k}:')
        #res.append(c1)
        trie = Trie()
        trie.add(c1)
        s = ['.'] * 5 + ['-']* 5
        perms = []
        for s in gen_perm(s, 0):
            perms.append(s)
        j = 0
        cnt = 1
        while cnt < n:
            s = perms[j]
            s = ''.join(s)
            j += 2
            if trie.find_prefix(s):
                continue
            res.append(s)
            trie.add(s)
            cnt += 1
    return res


buf = utils.read_file('/Users/admin/Downloads/second_second_meaning_validation_input.txt')
res = solve(buf)
utils.write_file('/Users/admin/Downloads/second_meaning_validation_output2.txt', res)




