
def power(x, y, p):
    res = 1
    while y:
        if (y & 1) != 0:
            res = (res *x) % p
        y >>= 1
        x = (x * x) % p
    return res

def inverse(x,p):
    return power(x,p-2,p)



class Hash:
    def __init__(self, s):
        self.mod1 = 10 ** 9 + 7
        self.mod2 = 10 ** 9 + 9
        self.p1 = 31
        self.p2 = 37
        self.hash1 = [0] * len(s)
        self.hash2 = [0] * len(s)
        self.hash_pair = []
        self.inv_size = 1
        self.inv_pow1 = [0] * len(s)
        self.inv_pow2 = [0] * len(s)
        self.length = len(s)
        h1 = 0
        h2 = 0
        pow1 = 1
        pow2 = 1
        for i in range(len(s)):
            h1 = (h1 + (ord(s[i]) - ord('a') + 1) * pow1) % self.mod1
            h2 = (h2 + (ord(s[i]) - ord('a') + 1) * pow2) % self.mod2
            pow1 = (pow1 * self.p1) % self.mod1
            pow2 = (pow2 * self.p2) % self.mod2
            self.hash1[i] = h1
            self.hash2[i] = h2

        self.hash_pair = (h1, h2)
        if self.inv_size < self.length:
            while self.inv_size < self.length:
                self.inv_size <<= 1
            self.inv_pow1 = [-1] * self.inv_size
            self.inv_pow2 = [-1] * self.inv_size
            self.inv_pow1[self.inv_size - 1] = inverse(power(self.p1,self.inv_size-1,self.mod1),self.mod1)
            self.inv_pow2[self.inv_size - 1] = inverse(power(self.p2, self.inv_size - 1, self.mod2), self.mod2)
            i = self.inv_size - 2
            while i >= 0 and self.inv_pow1[i] == -1:
                self.inv_pow1[i] = (self.inv_pow1[i + 1] * self.p1) % self.mod1
                self.inv_pow2[i] = (self.inv_pow2[i + 1] * self.p2) % self.mod2
                i -= 1

    def prefix(self, i):
        return (self.hash1[i], self.hash2[i])

    def substr(self, l, r):
        if l == 0:
            return (self.hash1[r],self.hash2[r])
        temp1 = self.hash1[r] - self.hash1[l - 1]
        temp2 = self.hash2[r] - self.hash2[l - 1]
        if temp1 < 0:
            temp1 += self.mod1
        if temp2 < 0:
            temp2 += self.mod2
        temp1 = (temp1 * self.inv_pow1[l]) % self.mod1
        temp2 = (temp2 * self.inv_pow2[l]) % self.mod2
        return (temp1, temp2)

    def __len__(self):
        return self.length


def query(hashes, l, r):
    l -= 1
    r -= 1
    lb = 0
    ub = min(len(hashes[l]), len(hashes[r]))
    max_len = 0
    while lb <= ub:
        mid = (lb + ub) >> 1
        if hashes[l].prefix(mid) == hashes[r].prefix(mid):
            if mid + 1 > max_len:
                max_len = mid + 1
            lb = mid + 1
        else:
            ub = mid - 1
    return max_len

arr = ['geeksforgeeks','geeks','hell','geeksforpeaks', 'hello']
q = [(1,2),(1,3),(3,5),(1,4)]
hashes = []
for s in arr:
    hashes.append(Hash(s))

for l,r in q:
    print(query(hashes, l,r))







