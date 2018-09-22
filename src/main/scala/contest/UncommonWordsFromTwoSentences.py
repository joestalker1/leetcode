class Solution:
    def uncommonFromSentences(self, a, b):
        if not b and not a:
            return []
        if not b:
            return a.split()
        if not a:
            return b.split()
        words1 = a.split()
        seen1 = {}
        for word in words1:
            if word not in seen1.keys():
                seen1[word] = 1
            else:
                seen1[word] += 1

        words2 = b.split()
        seen2 = {}
        for word in words2:
            if word not in seen2.keys():
                seen2[word] = 1
            else:
                seen2[word] += 1

        diff1 = (seen1.keys() - seen2.keys())
        diff2 = (seen2.keys() - seen1.keys())
        diff = diff1.union(diff2)
        res = []
        for word in diff:
            if word in seen1.keys() and seen1[word] == 1 or word in seen2.keys() and seen2[word] == 1:
                res.append(word)
        return res


sol = Solution()
print(sol.uncommonFromSentences("apple apple", "banana"))
print(sol.uncommonFromSentences("this apple is sour", "this apple is sweet"))