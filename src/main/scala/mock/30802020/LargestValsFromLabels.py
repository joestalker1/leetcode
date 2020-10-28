class Solution:
    def largestValsFromLabels(self, values, labels, num_wanted, use_limit):
        if not values or not labels:
            return 0
        val_lab = [[values[i], labels[i]] for i in range(len(values))]
        val_lab.sort(key=lambda x:x[0], reverse=True)
        res = 0
        lab_to_count = {}
        for v,l in val_lab:
            if num_wanted == 0:
                return res
            if l not in lab_to_count or lab_to_count[l] < use_limit:
                res += v
                lab_to_count[l] += 1
                num_wanted -= 1
        return res



