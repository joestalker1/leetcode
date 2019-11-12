class SuffixArray:
    def __init__(self):
        self.maxn = 200010
        self.ra = [0] * self.maxn
        self.sa = [0] * self.maxn
        self.lcp = [0] * self.maxn
        self.step = 0

    def cmp(self, a, b):
        if self.step == 1 or self.fc