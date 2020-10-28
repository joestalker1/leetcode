class Solution:
    def expressiveWords(self, S, words):
        def make_group(s):
            groups = []
            for ch in s:
                if not groups:
                    groups.append([ch])
                else:
                    if groups[-1][-1] == ch:
                        groups[-1].append(ch)
                    else:
                        groups.append([ch])
            return groups

        target_group = make_group(S)
        res = 0
        for word in words:
            word_group = make_group(word)
            if len(target_group) != len(word_group):
                continue
            stretchy = True
            for i in range(len(target_group)):
                tg = target_group[i]
                cg = word_group[i]
                if cg[0] != tg[0] or (len(tg) < 3 and len(tg) != len(cg)):
                    stretchy = False
                if not stretchy:
                    break
            if stretchy:
                res += 1
        return res





