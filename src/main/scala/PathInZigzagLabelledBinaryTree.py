from math import log

class Solution:
    def pathInZigZagTree(self, label):
        if label < 0:
            return []
        row = int(log(label, 2)) + 1
        #start label
        s = 2 ** (row - 1)
        #end label
        e = 2 * s - 1
        res = []
        #find pos
        pos = label - 1
        #pos is label - 1
        if row % 2 == 0:
            off = e - label
            pos = s - 1 + off
        while pos >= 0:
            label = pos + 1
            if row % 2 == 0:
                #numbers are from right to left
                #fix label
                off = label - s
                label = e - off
            if pos % 2 == 0:
                pos -= 2
            else:
                pos -= 1
            res.insert(0, label)
            pos //= 2
            row -= 1
            s //= 2
            e = s * 2 - 1
        return res


sol = Solution()
#print(sol.pathInZigZagTree(787046))
print(sol.pathInZigZagTree(26))
print(sol.pathInZigZagTree(14))








