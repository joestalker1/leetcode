from collections import defaultdict


class Solution:

    def get_key(self, s):
        key = []
        for i in range(1, len(s)):
            diff = ord(s[i]) - ord(s[i - 1])
            if diff < 0:
                diff += 26
            key.append(str(diff))
        return ''.join(key)

    def groupStrings(self, strings):
        if not strings:
            return []

        shifting_seq = defaultdict(list)
        for string in strings:
            k = self.get_key(string)
            shifting_seq[k].append(string)
        return shifting_seq.values()


sol = Solution()
print(sol.groupStrings(
    ["fpbnsbrkbcyzdmmmoisaa", "cpjtwqcdwbldwwrryuclcngw", "a", "fnuqwejouqzrif", "js", "qcpr", "zghmdiaqmfelr", "iedda",
     "l", "dgwlvcyubde", "lpt", "qzq", "zkddvitlk", "xbogegswmad", "mkndeyrh", "llofdjckor", "lebzshcb",
     "firomjjlidqpsdeqyn", "dclpiqbypjpfafukqmjnjg", "lbpabjpcmkyivbtgdwhzlxa", "wmalmuanxvjtgmerohskwil",
     "yxgkdlwtkekavapflheieb", "oraxvssurmzybmnzhw", "ohecvkfe", "kknecibjnq", "wuxnoibr", "gkxpnpbfvjm", "lwpphufxw",
     "sbs", "txb", "ilbqahdzgij", "i", "zvuur", "yfglchzpledkq", "eqdf", "nw", "aiplrzejplumda", "d",
     "huoybvhibgqibbwwdzhqhslb", "rbnzendwnoklpyyyauemm"]))
# ['a', 'aiplrzejplumda', 'cpjtwqcdwbldwwrryuclcngw', 'd', 'dclpiqbypjpfafukqmjnjg', 'dgwlvcyubde', 'eqdf', 'firomjjlidqpsdeqyn', 'fnuqwejouqzrif', 'fpbnsbrkbcyzdmmmoisaa', 'gkxpnpbfvjm', 'huoybvhibgqibbwwdzhqhslb', 'i', 'iedda', 'ilbqahdzgij', 'js', 'kknecibjnq', 'l', 'lbpabjpcmkyivbtgdwhzlxa', 'lebzshcb', 'llofdjckor', 'lpt', 'lwpphufxw', 'mkndeyrh', 'nw', 'ohecvkfe', 'oraxvssurmzybmnzhw', 'qcpr', 'qzq', 'rbnzendwnoklpyyyauemm', 'sbs', 'txb', 'wmalmuanxvjtgmerohskwil', 'wuxnoibr', 'xbogegswmad', 'yfglchzpledkq', 'yxgkdlwtkekavapflheieb', 'zghmdiaqmfelr', 'zkddvitlk', 'zvuur']

# ['a', 'd', 'i', 'l', 'js', 'nw', 'lpt', 'qzq', 'sbs', 'txb', 'eqdf', 'qcpr', 'iedda', 'zvuur', 'lebzshcb', 'mkndeyrh', 'ohecvkfe', 'wuxnoibr', 'lwpphufxw', 'zkddvitlk', 'kknecibjnq', 'llofdjckor', 'dgwlvcyubde', 'gkxpnpbfvjm', 'ilbqahdzgij', 'xbogegswmad', 'yfglchzpledkq', 'zghmdiaqmfelr', 'aiplrzejplumda', 'fnuqwejouqzrif', 'firomjjlidqpsdeqyn', 'oraxvssurmzybmnzhw', 'fpbnsbrkbcyzdmmmoisaa', 'rbnzendwnoklpyyyauemm', 'dclpiqbypjpfafukqmjnjg', 'yxgkdlwtkekavapflheieb', 'lbpabjpcmkyivbtgdwhzlxa', 'wmalmuanxvjtgmerohskwil', 'cpjtwqcdwbldwwrryuclcngw', 'huoybvhibgqibbwwdzhqhslb']
# [["a", "d", "i", "l"], ["eqdf", "qcpr"], ["lpt", "txb"], ["yfglchzpledkq", "zghmdiaqmfelr"],
#  ["kknecibjnq", "llofdjckor"], ["cpjtwqcdwbldwwrryuclcngw", "huoybvhibgqibbwwdzhqhslb"],
#  ["lbpabjpcmkyivbtgdwhzlxa", "wmalmuanxvjtgmerohskwil"], ["iedda", "zvuur"], ["js", "nw"], ["lebzshcb", "ohecvkfe"],
#  ["dgwlvcyubde", "ilbqahdzgij"], ["lwpphufxw", "zkddvitlk"], ["qzq", "sbs"],
#  ["dclpiqbypjpfafukqmjnjg", "yxgkdlwtkekavapflheieb"], ["mkndeyrh", "wuxnoibr"],
#  ["firomjjlidqpsdeqyn", "oraxvssurmzybmnzhw"], ["gkxpnpbfvjm", "xbogegswmad"],
#  ["fpbnsbrkbcyzdmmmoisaa", "rbnzendwnoklpyyyauemm"], ["aiplrzejplumda", "fnuqwejouqzrif"]]
print(sol.groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]))
