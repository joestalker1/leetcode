class Solution:

    def propogate(self, v, l,r):
        if self.lazy[v] == 0:
            return
        ln = r - l + 1
        if self.lazy[v] & 1:
            self.st[v] = ln - self.st[v]
        if l != r:
            self.lazy[v << 1] += self.lazy[v]
            self.lazy[v << 1 | 1] += self.lazy[v]
        self.lazy[v] = 0

    def update(self,l,r,v,sl,sr):
        self.propogate(v,sl,sr)
        if r < sl or l > sr or sl > sr:
            return
        if sl >= l and sr <= r:
            self.lazy[v] += 1
            self.propogate(v,sl,sr)
            return
        m = (sl + sr) // 2
        self.update(l,r,v<<1,sl,m)
        self.update(l,r,v<<1|1,m+1,sr)
        self.st[v] = self.st[v << 1] + self.st[v << 1|1]

    def query(self, l,r,v,sl,sr):
        self.propogate(v,sl,sr)
        if r < sl or l > sr or sl > sr:
            return 0
        if sl >= l and sr <= r:
            return self.st[v]
        m = (sl + sr) // 2
        return self.query(l,r,v<<1,sl,m) + self.query(l,r,v<<1|1,m+1,sr)

    def handleQuery(self, nums1,nums2,queries):
        n = len(nums1)
        self.st = [0] * (4 * n)
        self.lazy = [0] * (4 * n)
        total = 0
        for num in nums2:
            total += num
        ans = []
        for i in range(n):
            if nums1[i] == 1:
                self.update(i,i,1,0,n-1)
        for q in queries:
            if q[0] == 1:
                self.update(q[1],q[2],1,0,n-1)
            elif q[0] == 2:
                ones = self.query(0,n-1,1,0,n-1)
                total += ones * q[1]
            else:
                ans.append(total)
        return ans
