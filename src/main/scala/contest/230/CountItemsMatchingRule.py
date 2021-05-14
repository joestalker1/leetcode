class Solution:
    def countMatches(self, items, ruleKey, ruleValue):
        cnt = 0
        m = {'type':0, 'color':1,'name':2}
        for item in items:
            p = m[ruleKey]
            if item[p] == ruleValue:
                cnt += 1
        return cnt