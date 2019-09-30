class Solution:
    def longestStrChain(self, words):
        if not words:
            return False

        def is_pred(pred, succ):
            chars = [0] * 26
            for ch in words[pred]:
                chars[ord(ch) - ord('a')] += 1
            for ch in words[succ]:
                pos = ord(ch) - ord('a')
                chars[pos] -= 1
                if chars[pos] < -1:
                    return False
            zeros = 0
            ones = 0
            for a in chars:
                if a == -1:
                    ones += 1
                if a == 0:
                    zeros += 1
                if ones > 1:
                    return False
            return zeros == len(chars) - 1

        #sort by length
        words.sort(key=lambda s: len(s))
        dp = [1] * len(words)
        max_len = 1
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                if len(words[j]) > len(words[i]) + 1:
                    break
                if len(words[i]) < len(words[j]) and is_pred(i, j):
                    dp[j] = max(dp[j], dp[i] + 1)
                    max_len = max(max_len, dp[j])
        return max_len

sol = Solution()
arr = ["kwigbkfeqp","tpiufntqzo","blmwegckaplqwjpo","uiesdrhcbvbbk","przuvuo","kntmjgnqbxlwh","glac","uz","qqhw","gdtunmaw","neymepxl","eqtxh","qz","bek","xgadqztq","cicgtxs","grakdthb","kwigbkfeqop","uqyqhjqwegizcx","kewiygbkfejqop","tufntz","gulamac","sluiobdm","ujdyugagn","fuyz","eth","vzxiobwgyhrdkh","ikfjaivyvreql","jimpyin","cuotmvfqzizu","tkopssxh","gmwmzsowjf","nel","zo","kntmmjgnqbxtlwh","cyuicglbdtxwsu","vjrenjwntklm","uevrxuklobce","tkaopssxh","rwkedydnadd","uqyqhjqdwegizcx","ouethhse","zcmmrtilpti","tmfuxxyk","honyw","nyepl","qqhqwix","mjhg","gdtwunmaw","kigbkfeqp","wnyhsm","oeqatxhree","qyqhjqweizcx","xadqztq","wqnyghsmt","ndozeaylmetnpxlj","przuvuhob","wqnlyghnqsmtt","tkossxh","qyqhjqwix","epwcjxytvt","bexk","ga","em","zojodbw","gulmac","cizocgw","suibdm","nvcyutywhus","bwjofkuchx","f","pdtwv","dzohajcodbw","kuc","tpawplvfzlx","mg","re","oh","wciqob","el","wciqo","mftmgv","grakkdthtbd","cnbnyvuhmrj","odqphbhkf","oeqatxhre","sqzrlhs","bwsjofvkuptchx","xdqztq","tmv","kewigbkfejqop","faepomn","bdwwnalubrvxtdgu","cotmfqziz","lvzl","dmqz","hdmqz","gdigs","ujdyugag","mepjqbuvdku","g","kigbkeqp","oegqataxhree","zscinzobcgtwdwhn","fuaepwobimn","qf","cusotmvfqziknzu","qvroffuk","rweydnadd","zoow","meqcfzkbnrb","tpaplvzlx","zscinzocgwdwhn","zcmmrtilpt","ndeaymenpxlj","jimpn","wofkuchx","tkaopsssxh","vodwqphbhkfx","faepwoimn","gzenkasrciui","nyhm","tpufntqzo","ovqeyvxfdll","tufntzo","gmyrmf","vxobwgrdkh","faepwobimn","przujvuhobk","vzxobwgyrdkh","ksszdumgko","kewiylgbkfejqop","rey","vo","qqfe","moyddffrwwyzk","qzwsbnuejvsi","vodwqpzhbhjkfx","r","vttpoelti","sqzrlehhs","tpiuftntqzo","qfe","qyvsrofgnfuk","evxuklce","wiqo","prpzuujvuaxhkobk","gy","vnjxkjvmz","qroffuk","qqhwi","przuvuhobk","mfttmgvj","moydfrwzk","jibmpuyin","pwcytvt","eqtxhre","gcdtwunmaw","wfkucx","ryedhy","vttpolti","qyqhqwix","kutkavldvvqvp","el","tmfuxxyku","tplvzlx","gdtu","z","ksg","xmgadqzptq","qcqfre","zcmmrtiklpti","hobxltexk","vburq","funyz","kc","vjrenjwntklqm","wqnlyghnqsmt","sibdm","vodwqpzhbhkfx","zsnv","pouegzfyk","arci","vzxobwgyhrdkh","fetoesaot","riyedhy","cyuicgtxsu","gdtua","gchdtwgwunmaw","cuotmvfqziz","obltexk","epwcytvt","scinzocgw","ptwv","jimpuyin","uevrxukloce","tkqaopsssxh","pdtwdv","fetsaot","cyuicgldtxsu","przujvuaxhkobk","wciqoxb","gdtuna","lvzlx","ytpawcplvfzlx","uyugag","ksszdumugiko","bm","pgdmigs","grakdthtbd","uyz","zscinzobcgwdwhn","oeqataxhree","qzsbnuvs","gznkarciui","zoodw","jimpin","tqksugh","zuvo","tmgv","gdmigs","sluibdm","nvcxyzwyutywhus","bwsjofkuchx","fetsat","kgbeqp","neymenpxlj","vzxobwgrdkh","tpawcplvfzlx","qbzwsbnuejvsi","przuvuho","wqnlyguhnqsmtt","ujhadylujgaazgsn","axuelrnnnwhg","qbzwsbnuejvsmoi","qzsbnuvsi","yugag","bwsjofvkupchx","mqz","gchdtwunmaw","kntmmjgnqbxlwh","xfpt","vvburq","moydfrwk","qksgh","faepoimn","odwqphbhkfx","ryey","gchdtwwunmaw","uiesdrhcvbbk","qyqhjqwicx","yilxbltwwxh","jrenjwntkm","gzenkarciui","moyddffrhwwyezk","tqksugvhr","oveyvxfl","agmyrmf","scinzocgwdn","neymenpxl","gonpxzngjv","rwkeydnadd","zohjodbw","bdwwnalubvxtdgu","jrenjwntk","ovqheyvxubfdtll","qcqfqrezof","znkarcii","b","qzsnuvs","ndzeaylmenpxlj","tossxh","fetsa","przujvuxhkobk","ovqeyvxubfdll","tpufntzo","cuicgtxs","mv","vbur","moyddffrhwwyzk","yilxcbltwwxh","eqtxhe","zow","qbzwsbnuejvsoi","nvczwyutywhus","cyquicglbdtxwsu","evxukce","axuelrnnwhg","aci","ouemthhqse","wfkuchx","bwsjofvkmuptchx","mfjhg","bwsjofvkuchx","qffu","qyqhjqwegizcx","rzuvuo","uvo","qh","qvsrofgfuk","neymepl","mepjqybuvdku","sqzrlehs","cnbnyvumrj","qcqfqrezoif","gyrm","przujvuhkobk","cuotmvfqzinzu","gym","ujdylujgaagn","thdmmqz","honw","odwqphbhkf","ksszgko","qbzwsbnuejvsmvoi","m","gtu","qyvsrofgfuk","uqqyqhjqdwegizcx","obtexk","hobltexk","ftmgv","bwsjofvkmuptchxy","taynfxo","tqksugvhrc","jibmpduyin","vxue","zuvuo","gonpxzngv","gmpwamzsowjf","rwednadd","zv","tosh","pqdtwdv","zcmmrtsiklpti","tkqaopesssxh","ovqeyvxbfdll","gac","gsqzrlehhs","znv","cuotmvfqziknzu","ryedy","vnjoxkjvmz","pouegnzfyk","evrxuklce","ujdyujgagn","tmfnuxxyku","semj","xmgadvqzptq","cnnyvmrj","gonpxzvngjv","meqczkbnrb","bwofkuchx","fuvnyz","znarci","moydffrwzk","kwigbkfejqop","wqnyghnsmt","uiesdrehcbvobbk","qcqfreo","zohajodbw","nvcxyzwyutywhuhs","scinzocgwdwn","ksyszdumugiko","qfu","mjg","zsnuvs","eqth","ccgtxs","pgdmidtgs","rwednad","lel","cusotmvfqzwiknzu","znkarciui","o","qzsbnuevsi","veodwqpzhbhjkfx","jrenjwntklm","gmwamzsowjf","ndeymenpxlj","moydffrwwzk","nvczyutywhus","dzohajodbw","ujadylujgaazgsn","nvcytywhus","qcqfrezo","mfttmgv","tqksugvh","qksg","njxkjvmz","udyugag","qffuk","ksszdugko","wkuc","tmfxxyk","qqh","sbdm","rwedna","ovqheyvxubsfdtll","ndzeaymenpxlj","neyepl","qf","xgadqzptq","redna","pougzfyk","zarci","mftbtmgvj","taplvzlx","uiesdrhcbvobbk","ovqeyvxfdl","qcqfrezof","qvrofgfuk","scizocgw","mftbtmgvdj","rsgwmsted","ovqheyvxubfdll","oveyvxfdl","m","wi","znkarci","ikfjaivyvrql","pgdmidgs","btexk","cuotmfqziz","xdqzq","jimp","qqhqwi","lvz","ilojawyersju","wnyhm","gsqzrlenhhs","bu","wkucx","bdm","lsel","tpawplvzlx","ai","kntmmjognqbxtlwh","hkonyw","vxuce","zsnvs","qyqhjqweicx","nyel","cyuicgtxs","qzsbnuejvsi","ujadylujgaagsn","thdmqz","ilojawyersu","uevirxuklobce","qrffuk","zoodbw","sem","cyuicgldtxwsu","wnyhsmt","prpzujvuaxhkobk","uesdrhcvbbk","vhvburq","ndzeaylmetnpxlj","ksszdgko","scinzocgwd","cyuicgltxsu","ptw","mplaxm","scinzocgwdwhn","ytpawcplvifzlx","evxuce","bur","kigbeqp","ksszdumugko","cnnyvumrj","toh","kewiylgbkfejqfop","gulac","pugzfyk","nvcyzwyutywhus","ouemthhse","wqnyghnqsmt","b","ujdylujgagn","tlvzlx","pgidmidtgs","eqatxhre","gmyrm","dqzq","oveyvxl","vttpoeltci","gk","wqnyhsmt","zcmmrtsitklpti","iaxuelrnnnwhg","gdtunma","ujadylujgaagn","tqksgh","moydffrwwyzk","mfftbtmgvdj","wio","fetosaot","grakdthtb","nxmrvm","evrxukloce","ikfjaivyrql","tosxh","grakkbdthtbd","epwcxytvt","blmwegckaplwjpo","qcqfe"]
print(sol.longestStrChain(arr))#16
#7
#arr = ["gr","grukmj","gruj","grukkmj","grukj","gru"]
#arr = ["czvh","zczpzvdhx","zczpzvh","zczpzvhx","zcpzvh","zczvh", "zczpzfvdhx"]
#arr = ["ksqvsyq","ks","kss","czvh","zczpzvdhx","zczpzvh","zczpzvhx","zcpzvh","zczvh","gr","grukmj","ksqvsq","gruj","kssq","ksqsq","grukkmj","grukj","zczpzfvdhx","gru"]
#print(sol.longestStrChain(arr))
print(sol.longestStrChain(["a","b","ba","bca","bda","bdca"]))


# nel
# nyel
# nyepl
# neyepl
# neymepl
# neymepxl
# neymenpxl
# neymenpxlj
# ndeymenpxlj
# ndeaymenpxlj
# ndzeaymenpxlj
# ndzeaylmenpxlj
# ndzeaylmetnpxlj
# ndozeaylmetnpxlj


