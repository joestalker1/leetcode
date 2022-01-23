
class Solution:
    def __init(self):
        self.timeGap = 0
        self.maxTimeGap = 0
        self.caseNo = 0

    def greedyLanding(self, a, b, n, order):
        lastLanding = a[order[0]]
        for i in range(1, n):
            targetLandingTime = lastLanding + self.timeGap
            if targetLandingTime <= b[order[i]]:
                lastLanding = max(a[order[i]], targetLandingTime)
            else:
                return 1 # to reduce timeGap
        return lastLanding - b[order[n - 1]] # increase timeGap

    def all_perm(self, order):
        def perm(i, res):
            if i == len(order):
                res.append(order[:])
                return res
            for j in range(i, len(order)):
                order[i],order[j] = order[j],order[i]
                perm(i + 1 ,res)
                order[i], order[j] = order[j], order[i]
        res = []
        return perm(0, res)

    def run(self):
        a = [0] * 8
        b = [0] * 8
        order = [i for i in range(9)]

        #fill in a and b arrays
        perms = self.all_perm(order)
        while len(perms):
            lo_val = 0
            hi_val = 86400
            perm = perms.pop(0)
            while abs(lo_val + hi_val) >= (10 ** -3):
                self.timeGap = lo_val + (hi_val - lo_val) / 2
                ret_val = self.greedyLanding(a, b, 8, perm)
                if ret_val <= (10 ** -2):
                    lo_val = self.timeGap
                else:
                    hi_val = self.timeGap
            self.maxTimeGap = max(self.maxTimeGap, self.timeGap)
        self.maxTimeGap += 0.5
        return self.maxTimeGap




