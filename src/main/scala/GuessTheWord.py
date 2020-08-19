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
        # number matches between i and j words in wordlist
        self.h = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                matched = 0
                for k in range(len(wordlist[0])):
                    if wordlist[i][k] == wordlist[j][k]:
                        matched += 1
                self.h[i][j] = matched
        # possible holds indexes of possible words
        possible = [i for i in range(n)]
        # used words
        path = set()
        # try every words
        while possible:
            # find guess, it's index
            guess = self.solve(possible, path)
            # try this guess
            match = master.guess(wordlist[guess])
            # if matched 6 chars, return this word
            if match == len(wordlist[0]):
                return len(wordlist[0])
            # form new possible list
            possible2 = []
            for j in possible:
                # get words having matched chars with guess
                if match == self.h[guess][j]:
                    possible2.append(j)
            possible = possible2
            # mark guess as used
            path.add(guess)
        return -1

    def solve(self, possible, path=()):
        # find new words
        max_min_len = len(possible)
        # new word index
        ans = -1
        for guess in range(len(self.h)):
            # consider candidates from self.h
            if guess not in path:
                # if candidate hasn't be not used
                # check if it matches with words from possible
                groups = [[] for _ in range(7)]
                for j in possible:
                    if j != guess:
                        # group by number of matched chars
                        groups[self.h[guess][j]].append(j)
                # take group with max cardinality
                maxgroup = max(groups, key=len)
                # if group has less member, it will be our new group and guess is new result
                if len(maxgroup) < max_min_len:
                    max_min_len = len(maxgroup)
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
