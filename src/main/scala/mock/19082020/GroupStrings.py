from collections import defaultdict

class Solution:
    def to_code(self, ch):
        return ord(ch) - ord('a')

    def is_next(self, word1, word2):
        for i in range(len(word1)):
            ch1 = word1[i]
            ch2 = word2[i]
            if i == 0:
                if ch1 > ch2:
                    return False
            else:
                d1 = abs(self.to_code(word1[-1]) - self.to_code(word2[-1]))
                d2 = abs(self.to_code(ch1) - self.to_code(ch2))
                if not (word1[-1] <= ch1 and word2[-1] <= ch2 or word1[-1] > ch1 and word2[-1] > ch2 or word1[
                    -1] <= ch1 and word2[-1] > ch2 and ch1 == 'z'):
                    return False
        return True

    def groupStrings(self, strings):
        group_by_len = defaultdict(list)
        for string in strings:
            group_by_len[len(string)].append(string)

        res = []
        for k, words in group_by_len.items():
            words.sort()
            seen = set()
            for i in range(len(words)):
                seen.add(i)
                seq = [words[i]]
                for j in range(len(words)):
                    if j in seen:
                        continue
                    if self.is_next(seq[-1], words[j]):
                        seq.append(words[j])
                        seen.add(j)
                res.append(seq)
        return res


sol = Solution()
print(sol.groupStrings(
    ["fpbnsbrkbcyzdmmmoisaa", "cpjtwqcdwbldwwrryuclcngw", "a", "fnuqwejouqzrif", "js", "qcpr", "zghmdiaqmfelr", "iedda",
     "l", "dgwlvcyubde", "lpt", "qzq", "zkddvitlk", "xbogegswmad", "mkndeyrh", "llofdjckor", "lebzshcb",
     "firomjjlidqpsdeqyn", "dclpiqbypjpfafukqmjnjg", "lbpabjpcmkyivbtgdwhzlxa", "wmalmuanxvjtgmerohskwil",
     "yxgkdlwtkekavapflheieb", "oraxvssurmzybmnzhw", "ohecvkfe", "kknecibjnq", "wuxnoibr", "gkxpnpbfvjm", "lwpphufxw",
     "sbs", "txb", "ilbqahdzgij", "i", "zvuur", "yfglchzpledkq", "eqdf", "nw", "aiplrzejplumda", "d",
     "huoybvhibgqibbwwdzhqhslb", "rbnzendwnoklpyyyauemm"]))
