from collections import defaultdict

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList):
        if not wordList or len(wordList[0]) == 0:
            return []
        adj_list = defaultdict(list)

        def find_neighbors(word, word_list):
            chars = list(word)
            for i, ch in enumerate(chars):
                prev = ch
                # change char at pos i by a ...z
                for c in range(ord('a'), ord('z') + 1):
                    chars[i] = chr(c)
                    new_word = ''.join(chars)
                    # if c is the same as original or word is not in word_list, lets skip it.
                    if c == prev or new_word not in word_list:
                        continue
                    yield new_word
                chars[i] = prev

        def dfs(adj_list, src, dest, cur_path, shortest_path,color):
            if src == dest:
                shortest_path.append(cur_path)
            if src != beginWord:
                color[src] = 1
            if src not in adj_list:
                return
            for w in adj_list[src]:
                if color[w] == 0:
                    dfs(adj_list, w, dest, cur_path + [w], shortest_path,color)
            if src != beginWord:
                color[src] = 2

        def bfs(adj_list, begin_word, word_list):
            if begin_word in word_list:
                word_list.discard(begin_word)
            proc = set()
            q = [begin_word]
            proc.add(begin_word)
            while q:
                visited = set()
                n = len(q)
                for i in range(n):
                    cur_word = q.pop(0)
                    # find which words differ by one cahr
                    for w in find_neighbors(cur_word, word_list):
                        visited.add(w)
                        adj_list[cur_word].append(w)
                        if w not in proc:
                            q.append(w)
                            proc.add(w)
                for w in visited:
                    if w in word_list:
                        word_list.discard(w)

        word_list = set(wordList)
        # fill up adj_list
        bfs(adj_list, beginWord, word_list)
        cur_path = [beginWord]
        shortest_path = []
        color = defaultdict(int)
        dfs(adj_list, beginWord, endWord, cur_path, shortest_path,color)
        return shortest_path


sol = Solution()
print(sol.findLadders("aaaaa","ggggg",["aaaaa","caaaa","cbaaa","daaaa","dbaaa","eaaaa","ebaaa","faaaa","fbaaa","gaaaa","gbaaa","haaaa","hbaaa","iaaaa","ibaaa","jaaaa","jbaaa","kaaaa","kbaaa","laaaa","lbaaa","maaaa","mbaaa","naaaa","nbaaa","oaaaa","obaaa","paaaa","pbaaa","bbaaa","bbcaa","bbcba","bbdaa","bbdba","bbeaa","bbeba","bbfaa","bbfba","bbgaa","bbgba","bbhaa","bbhba","bbiaa","bbiba","bbjaa","bbjba","bbkaa","bbkba","bblaa","bblba","bbmaa","bbmba","bbnaa","bbnba","bboaa","bboba","bbpaa","bbpba","bbbba","abbba","acbba","dbbba","dcbba","ebbba","ecbba","fbbba","fcbba","gbbba","gcbba","hbbba","hcbba","ibbba","icbba","jbbba","jcbba","kbbba","kcbba","lbbba","lcbba","mbbba","mcbba","nbbba","ncbba","obbba","ocbba","pbbba","pcbba","ccbba","ccaba","ccaca","ccdba","ccdca","cceba","cceca","ccfba","ccfca","ccgba","ccgca","cchba","cchca","cciba","ccica","ccjba","ccjca","cckba","cckca","cclba","cclca","ccmba","ccmca","ccnba","ccnca","ccoba","ccoca","ccpba","ccpca","cccca","accca","adcca","bccca","bdcca","eccca","edcca","fccca","fdcca","gccca","gdcca","hccca","hdcca","iccca","idcca","jccca","jdcca","kccca","kdcca","lccca","ldcca","mccca","mdcca","nccca","ndcca","occca","odcca","pccca","pdcca","ddcca","ddaca","ddada","ddbca","ddbda","ddeca","ddeda","ddfca","ddfda","ddgca","ddgda","ddhca","ddhda","ddica","ddida","ddjca","ddjda","ddkca","ddkda","ddlca","ddlda","ddmca","ddmda","ddnca","ddnda","ddoca","ddoda","ddpca","ddpda","dddda","addda","aedda","bddda","bedda","cddda","cedda","fddda","fedda","gddda","gedda","hddda","hedda","iddda","iedda","jddda","jedda","kddda","kedda","lddda","ledda","mddda","medda","nddda","nedda","oddda","oedda","pddda","pedda","eedda","eeada","eeaea","eebda","eebea","eecda","eecea","eefda","eefea","eegda","eegea","eehda","eehea","eeida","eeiea","eejda","eejea","eekda","eekea","eelda","eelea","eemda","eemea","eenda","eenea","eeoda","eeoea","eepda","eepea","eeeea","ggggg","agggg","ahggg","bgggg","bhggg","cgggg","chggg","dgggg","dhggg","egggg","ehggg","fgggg","fhggg","igggg","ihggg","jgggg","jhggg","kgggg","khggg","lgggg","lhggg","mgggg","mhggg","ngggg","nhggg","ogggg","ohggg","pgggg","phggg","hhggg","hhagg","hhahg","hhbgg","hhbhg","hhcgg","hhchg","hhdgg","hhdhg","hhegg","hhehg","hhfgg","hhfhg","hhigg","hhihg","hhjgg","hhjhg","hhkgg","hhkhg","hhlgg","hhlhg","hhmgg","hhmhg","hhngg","hhnhg","hhogg","hhohg","hhpgg","hhphg","hhhhg","ahhhg","aihhg","bhhhg","bihhg","chhhg","cihhg","dhhhg","dihhg","ehhhg","eihhg","fhhhg","fihhg","ghhhg","gihhg","jhhhg","jihhg","khhhg","kihhg","lhhhg","lihhg","mhhhg","mihhg","nhhhg","nihhg","ohhhg","oihhg","phhhg","pihhg","iihhg","iiahg","iiaig","iibhg","iibig","iichg","iicig","iidhg","iidig","iiehg","iieig","iifhg","iifig","iighg","iigig","iijhg","iijig","iikhg","iikig","iilhg","iilig","iimhg","iimig","iinhg","iinig","iiohg","iioig","iiphg","iipig","iiiig","aiiig","ajiig","biiig","bjiig","ciiig","cjiig","diiig","djiig","eiiig","ejiig","fiiig","fjiig","giiig","gjiig","hiiig","hjiig","kiiig","kjiig","liiig","ljiig","miiig","mjiig","niiig","njiig","oiiig","ojiig","piiig","pjiig","jjiig","jjaig","jjajg","jjbig","jjbjg","jjcig","jjcjg","jjdig","jjdjg","jjeig","jjejg","jjfig","jjfjg","jjgig","jjgjg","jjhig","jjhjg","jjkig","jjkjg","jjlig","jjljg","jjmig","jjmjg","jjnig","jjnjg","jjoig","jjojg","jjpig","jjpjg","jjjjg","ajjjg","akjjg","bjjjg","bkjjg","cjjjg","ckjjg","djjjg","dkjjg","ejjjg","ekjjg","fjjjg","fkjjg","gjjjg","gkjjg","hjjjg","hkjjg","ijjjg","ikjjg","ljjjg","lkjjg","mjjjg","mkjjg","njjjg","nkjjg","ojjjg","okjjg","pjjjg","pkjjg","kkjjg","kkajg","kkakg","kkbjg","kkbkg","kkcjg","kkckg","kkdjg","kkdkg","kkejg","kkekg","kkfjg","kkfkg","kkgjg","kkgkg","kkhjg","kkhkg","kkijg","kkikg","kkljg","kklkg","kkmjg","kkmkg","kknjg","kknkg","kkojg","kkokg","kkpjg","kkpkg","kkkkg","ggggx","gggxx","ggxxx","gxxxx","xxxxx","xxxxy","xxxyy","xxyyy","xyyyy","yyyyy","yyyyw","yyyww","yywww","ywwww","wwwww","wwvww","wvvww","vvvww","vvvwz","avvwz","aavwz","aaawz","aaaaz"]))