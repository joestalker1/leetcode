from collections import defaultdict, Counter


class Solution:
    def longestStrChain(self, words):
        if not words or len(words) == 0:
            return 0

        def differs_by_one(word, subword):
            for i in range(len(word)):
                cand = word[0:i] + word[i + 1:]
                if cand == subword:
                    return True
            return False

        word_by_len = defaultdict(list)
        for word in words:
            word_by_len[len(word)].append(word)

        max_len = 1
        length = {word: 1 for word in words}
        for k in range(min(word_by_len.keys())+1, max(word_by_len.keys()) + 1):
            for word in word_by_len[k]:
                for subword in word_by_len[k - 1] :
                    if differs_by_one(word, subword) and length[word] < length[subword] + 1:
                        length[word] = max(length[word], length[subword] + 1)
                        max_len = max(max_len, length[word])
        return max_len

sol = Solution()
print(sol.longestStrChain(
    ["uiykgmcc", "jrgbss", "mhkqodcpy", "lkj", "bwqktun", "s", "nrctyzifwytjblwy", "wrp", "scqlcwmxw", "irqvnxdcxoejuu",
     "gmlckvofwyifmrw", "wbzbyrcppaljigvo", "lk", "kfeouqyyrer", "efzzpvi", "ubkcitcmwxk", "txihn", "mdwdmbtx",
     "vuzvcoaif", "jwmboqvhpqodsj", "wscfvrfl", "pzye", "waxyoxftvrgqmkg", "wwdidopozinxxn", "dclpg", "xjsvlxktxs",
     "ajj", "pvsdastm", "tatjxhygidhn", "feafycxdxagn", "irqvnxxoeuu", "kwjo", "tztoovsyfwz", "prllrw", "sclmx",
     "bbmjnwaxcwaml", "gl", "wiax", "uzvcoaif", "ztovyfwz", "qxy", "zuexoxyp", "qxyyrl", "pvsdasvtm", "femafycxdxaagn",
     "rspvccjcm", "wvyiax", "vst", "efzi", "fjmdcc", "icsinrbpql", "ctybiizlcr", "ntyzfwytjblw", "tatjxhygidhpn", "e",
     "kykizdandafusu", "pnepuwcsxl", "kfeuqyyrer", "afplzhbqguu", "hvajtj", "prll", "ildzdimea", "zueoxp", "ezi", "lqr",
     "jkaagljikwamaqvf", "mlzwhkxsn", "rspvccbcjjtcm", "wscfvrl", "m", "msygukwlkrqboc", "pifojogoveub", "bkcmwx",
     "jercgybhss", "wrpi", "aicsinkgrbpqli", "aplzbuu", "sclcmxw", "atpepgsz", "govrcuuglaer", "bdxjpsvlxkytxs",
     "uikgm", "bm", "wvyhiqax", "znvaasgfvqi", "hatpepgsz", "hrzebpa", "bnfz", "lybtqrfzw", "taxhygihn", "bjnfzk",
     "mhqp", "ide", "znvcaasgfvqi", "ftv", "afplzhbqsguuu", "thn", "pdbccbe", "mxevopfoimgjww", "fjmdrcce",
     "rspvccjjcm", "jv", "motnfwohwule", "xjsvlxtxs", "bqeb", "eug", "jftavwgl", "rzebpa", "lybtqrfazw", "zuexoxp",
     "jercgybhsys", "hajtj", "bkcitcmwxk", "mbpvxsdastvtm", "mowlznwhkxsn", "dvenn", "rsacxe", "tatjxhygihn",
     "cotybiizlcr", "bbmnaxaml", "pkwrpsi", "nqpdbccbkxens", "mbpbovxsdastvtm", "mj", "pxpsvikwekuq", "qeug",
     "dmelddga", "aicsinkgrbpxqli", "bdxjpsvlxktytxs", "pkrllrxw", "jkgljikwmaqf", "iddie", "ctybiizcr", "nyzfwytjblw",
     "yvuhmiuehspi", "keuqre", "wzbypaigvo", "sck", "uzcoaf", "dlpg", "ubkcpitlscmwxk", "molzwhkxsn", "pepuwcsxl",
     "laplm", "dclpgc", "mahkxqodcpy", "sclcmx", "hvrzebpaz", "bgovrcuuglaer", "clazpulmw", "yvuyhmiuehspiq",
     "wzbycpaljigvo", "sceqalciwmxw", "hjytflmvsgv", "u", "hjyvxytfflhmvsgv", "jkgjikwmaqf", "fefycxdxagn", "ftvw",
     "ofncgxrkqvcr", "spvcjc", "pvsdastvtm", "kykzdandaus", "wbzbycppaljigvo", "haytpepgsz", "jmowlznwhkxsn",
     "aplzhbguu", "zvyz", "nfvqi", "jfvtavwsgl", "xejnllhfulns", "zhhvbiqiw", "jkgljikwmaqvf", "tyizc", "irqvnxcxoejuu",
     "clvazzpulmw", "oncgxrqvcr", "qlupvpdkhrm", "mtnfwohwule", "wwdidopzozinxxn", "auiykgmcc", "wscfvrfyl",
     "pfksmrullrxw", "jwmoqvhpqods", "ftavwg", "iddiea", "kcmw", "ykkwjwo", "pe", "aplzbguu", "eu", "bbmnaxal",
     "ntyswtnlab", "zhhhvbhbiqiw", "jwmoqvpqods", "kykzdndaus", "bbmjnaxcwaml", "zunvcaasgfvqi", "icsingrbpql",
     "sceqalciwmsxyw", "yvuhmiuehsp", "bxjsvlxktxs", "waxoxftvrgqmkg", "cogxxpaknks", "scllvazzpulmw", "tatjxhygeidhpn",
     "ftvwg", "tyz", "nafvqi", "oby", "pgzpkhqog", "irqvnxxoejuu", "oxwpkxlakcp", "bnf", "oxwnpkxlakcp", "bwqktu",
     "ufybbaozoqk", "ntydswtnlab", "zvyfz", "znaafvqi", "npdbccbke", "mhkqocpy", "kuq", "bjnfz", "taxhyihn", "kwrpsi",
     "qifepmcatbdjlf", "lzwhks", "kfeuqre", "mxevopfoimgww", "spvcjcm", "oncgxrkqvcr", "jftavwsgl", "soifcbya",
     "jpzyeg", "jwmboqvhpqods", "lapulm", "jrgbhss", "xejfnllhfulns", "zhhhvbbiqiw", "km", "kuqre", "scxlzlvazzpulmw",
     "ztvyfwz", "wbzbycpaljigvo", "rzbpa", "vsastm", "uybaooqk", "dn", "ykwjwo", "ufybmvbaozoqk", "nknm",
     "mbpvsdastvtm", "dpgzpxykhqog", "wzbypajigvo", "bnjnfzk", "eollbigtftpdrd", "zhbiqiw", "yvuhiuehp",
     "zhhhvbhbiqiwg", "pfksrullrxw", "pzyeg", "aplzhbqguu", "z", "hvrzecbpazw", "clvazpulmw", "tajxhygihn",
     "pgzpxykhqog", "fefyxdxagn", "wimomuvhn", "lqrzw", "xejnlhfulns", "jhrc", "xsxxs", "slmx", "jrgss", "uikgmc",
     "ncgqvcr", "womuhn", "aryouvtnmme", "uzco", "zhhhvbiqiw", "hjytflhmvsgv", "znvaasfvqi", "kuqr", "ojrpp",
     "ztoovyfwz", "zvz", "pxpsviweuq", "ufybaooqk", "xy", "jfvvtavwksvgl", "raiachv", "bmnaxl", "rspvccjjtcm",
     "pgzpxkhqog", "xhbtfnqebaj", "sceqalciwmsxw", "jssctk", "uzvcoaf", "fefydxagn", "jhrvc", "mbj", "raiahv",
     "nrtyzifwytjblwy", "mhqcp", "jkgjkwmaqf", "wscfvrfylhi", "lqrz", "ahabucermswyrvl", "wxoxftvrgqmkg", "ku", "uyaoq",
     "mhqocp", "ykwjo", "vstm", "ofncgxrkqvcwr", "dqvh", "taxyihn", "idie", "bwqtu", "tztoovyfwz", "rspvcccjjtcm",
     "uojrpp", "wmomuhn", "cotycbiizlxcr", "nrtyzfwytjblw", "ocbya", "sceqlciwmxw", "ajtj", "rspvccbcjjthcm",
     "kfeuqyyre", "dmelddg", "txyihn", "ubkcitlscmwxk", "ntyswtnla", "bdxjpstvlxktytxs", "odqdvbh", "pxpsvikeewekuq",
     "mdwdmbdtux", "vs", "bma", "wzbypigvo", "qxyy", "vsstm", "hbtnqeba", "hrzebpaz", "xhbtfnjsqebbaj", "ahaucermswyrv",
     "ddmbtx", "zhhbiqiw", "pxpsvikewekuq", "odqdvgbh", "bxjpsvlxktxs", "jsck", "fjmdc", "mdwdmbdtx", "jqxyyrl",
     "pxpsvikweuq", "ctybizcr", "dqvbh", "lpl", "lqrfzw", "ufybaozoqk", "znvaafvqi", "yvuhmiuehp", "hvrzebpazw",
     "pfksrllrxw", "alzuu", "xjsvxtxs", "afplzhbqguuu", "icsingrbpqli", "hjxytflhmvsgv", "femafycxdxagn", "uyaoqk",
     "gmlckvofwyifrw", "cinrbpql", "jrcgbhss", "oxwpkxlkcp", "jkagljikwamaqvf", "eollbigtftpdrdy", "rspvcjcm", "socbya",
     "clapulm", "qeb", "kwrpi", "efzpi", "hbtfnqebaj", "kykizdnandafusu", "sclvazzpulmw", "efzzpvvi", "jfvvtavwsvgl",
     "mhqocpy", "v", "mbpbvxsdastvtm", "irqvnxouu", "hvaajtj", "ofnlcgxrkqvcwr", "hbtqeba", "hbtqeb", "jwmqpds",
     "ntrnlhujdslco", "zv", "npdbccbken", "mhp", "ddb", "prllw", "mddmbtx", "clazpulm", "cogxxpaknkse", "bkitcmwxk",
     "oxwpklkcp", "tyiz", "jwmqvpqods", "waxyoxftvrgqmkgb", "afplzhbbqsgujuu", "bwtu", "jercgbhss", "rsacx",
     "mahkqodcpy", "cotycbiizlcr", "ahabucermswyrv", "lupvpkhr", "dvnn", "b", "atpepsz", "ncgxqvcr", "qe",
     "ubkcitlcmwxk", "lyqrfzw", "wimomuhn", "bbmnaxl", "motnfwohrwule", "yvuyhmiuehspi", "jfvvtavwsgl", "rac",
     "fefdxagn", "bwqkctun", "uotjrpp", "ddbtx", "afplzhbbqsguuu", "xss", "xsxs", "wvyiqax", "kykizdandaus",
     "npdbccbkens", "r", "oxwnpkxjlakcp", "tzmteoovsyfwz", "kykizdnandafuspu", "ahabulcermswyrvl", "xjsxxs", "qxyyr",
     "ck", "xhbtfnqebbaj", "nqpdbccbkens", "mpvsdastvtm", "zuexqoxyp", "gmlkvofwyifrw", "kmw", "txhn", "kykizdandausu",
     "molznwhkxsn", "lupvpdkhr", "jwmqvpds", "bktcmwx", "wyiax", "hzvaajtj", "ddbx", "pifojogveub", "naafvqi",
     "motnfwjohrwule", "odqvbh", "aicsingrbpqli", "jopzyeg", "lybtqrfazrw", "pijogveub", "xzejfnllhfulns",
     "scxllvazzpulmw", "irqyvnxdcxfoejuu", "cogxpaknks", "pdkwrpsi", "wzbycpajigvo", "xjsxtxs", "irqvnxdcxfoejuu",
     "xhbtfnjqebbaj", "uybaoqk", "oncgxqvcr", "aj", "pepuwsxl", "lytqrfzw", "nkm", "jrgs", "pkrllrw", "wscfvrfyli",
     "bbmjnaxcaml", "jftavwg", "vuzvcozaif", "pifjogveub", "cmogxxpaknkse", "cinrbql", "scqlciwmxw", "ztvyfz",
     "mxyevopfoimgjpww", "soicbya", "lupvpdkhrm", "ahaucermsyrv", "ufybmvbaouzoqk", "bdxjpsvlxktxs", "hjxytfflhmvsgv",
     "hjvxytfflhmvsgv", "nqpdbccbzkxens", "wr", "kykzdndus", "iddimea", "fjmdrcc", "efzzpi", "vsdastm", "btqeb",
     "pfkrllrxw", "ocby", "irqvnxxouu", "ildzpdimea", "lzwhkxsn", "ilddimea", "ufybvbaozoqk", "mxyevopfoimgjww", "jhr",
     "kcmwx", "dvn", "uzcof", "glw", "hbtnqebaj", "riahv", "w", "qeugv", "kfeuqyre", "ilrdzpdimea", "lplm", "icinrbpql",
     "scqlcmxw", "bbmjnaxaml", "e", "rsac", "bf", "jwmqvpqds", "tzteoovsyfwz", "rc", "lzwhkxs", "jkgljikwamaqvf",
     "tybizc", "aplzuu", "nrtyzifwytjblw", "pze", "bktcmwxk", "uiykgmc", "jsctk", "npdbccbe", "tybizcr"]))  # 15
# print(sol.longestStrChain(
#     ["sgtnz", "sgtz", "sgz", "ikrcyoglz", "ajelpkpx", "ajelpkpxm", "srqgtnz", "srqgotnz", "srgtnz",
#      "ijkrcyoglz"]))  # 16
print(sol.longestStrChain(["a", "b", "ba", "bca", "bda", "bdca"]))  # 4