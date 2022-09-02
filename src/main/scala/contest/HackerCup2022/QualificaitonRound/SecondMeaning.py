import math
import utils
import random

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


def bin_entropy(n):
    return n * int(math.log(4 * n,2)) - 2 ** int(math.log(2*n,2))

def solve(buf):
    l = 0
    t = int(buf[l])
    l += 1
    res = []
    max_val = 10 ** 9 + 7
    for k in range(1, t + 1):
        n = int(buf[l])
        l += 1
        c1 = buf[l].strip()
        l += 1
        res.append(f'Case #{k}:')
        #res.append(c1)
        trie = Trie()
        trie.add(c1)
        cnt = 1
        while cnt < n:
            i = random.randint(10, max_val)
            a = bin_entropy(i)
            code = []
            while a:
                if a & 1 == 1:
                    code.append('-')
                else:
                    code.append('.')
                a = a >> 1
            s = ''.join(code[:10])
            if trie.find_prefix(s):
                continue
            cnt += 1
            res.append(s)
            trie.add(s)
    return res


buf = utils.read_file('/Users/admin/Downloads/second_second_meaning_validation_input.txt')
res = solve(buf)
utils.write_file('/Users/admin/Downloads/second_meaning_validation_output.txt', res)




