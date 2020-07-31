class Master:
    def __init__(self, sec):
        self.secret = sec

    def guess(self, word: str) -> int:
        match = 0
        for i in range(len(word)):
            if word[i] == self.secret[i]:
                match += 1
        return match

class Solution(object):
    def findSecretWord(self, wordlist, master):
        n = len(wordlist)
        self.h = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                c = 0
                for k in range(len(wordlist[0])):
                    if wordlist[i][k] == wordlist[j][k]:
                        c += 1
                self.h[i][j] = c
        possible = [i for i in range(n)]
        path = set()
        while possible:
            guess = self.solve(possible, path)
            match = master.guess(wordlist[guess])
            if match == len(wordlist[0]):
                return len(wordlist[0])
            possible2 = []
            for j in possible:
                if match == self.h[guess][j]:
                    possible2.append(j)
            possible = possible2
            path.add(guess)
        return -1

    def solve(self, possible, path = ()):
        if len(possible) <= 2:
            return possible[0]
        ansgrp = possible
        ans = -1
        for guess in range(len(self.h)):
            if guess not in path:
                groups = [[] for _ in range(7)]
                for j in possible:
                    if j != guess:
                        groups[self.h[guess][j]].append(j)
                maxgroup = max(groups, key = len)
                if len(maxgroup) < len(ansgrp):
                    ansgrp = maxgroup
                    ans = guess
        return ans


arr = ["gaxckt", "trlccr", "jxwhkz", "ycbfps", "peayuf", "yiejjw", "ldzccp", "nqsjoa", "qrjasy", "pcldos", "acrtag",
       "buyeia", "ubmtpj", "drtclz", "zqderp", "snywek", "caoztp", "ibpghw", "evtkhl", "bhpfla", "ymqhxk", "qkvipb",
       "tvmued", "rvbass", "axeasm", "qolsjg", "roswcb", "vdjgxx", "bugbyv", "zipjpc", "tamszl", "osdifo", "dvxlxm",
       "iwmyfb", "wmnwhe", "hslnop", "nkrfwn", "puvgve", "rqsqpq", "jwoswl", "tittgf", "evqsqe", "aishiv", "pmwovj",
       "sorbte", "hbaczn", "coifed", "hrctvp", "vkytbw", "dizcxz", "arabol", "uywurk", "ppywdo", "resfls", "tmoliy",
       "etriev", "oanvlx", "wcsnzy", "loufkw", "onnwcy", "novblw", "mtxgwe", "rgrdbt", "ckolob", "kxnflb", "phonmg",
       "egcdab", "cykndr", "lkzobv", "ifwmwp", "jqmbib", "mypnvf", "lnrgnj", "clijwa", "kiioqr", "syzebr", "rqsmhg",
       "sczjmz", "hsdjfp", "mjcgvm", "ajotcx", "olgnfv", "mjyjxj", "wzgbmg", "lpcnbj", "yjjlwn", "blrogv", "bdplzs",
       "oxblph", "twejel", "rupapy", "euwrrz", "apiqzu", "ydcroj", "ldvzgq", "zailgu", "xgqpsr", "wxdyho", "alrplq",
       "brklfk"]

master = Master("hbaczn")
sol = Solution()
print(sol.findSecretWord(arr, master))
