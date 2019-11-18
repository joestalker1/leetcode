from collections import defaultdict

class Solution(object):
    def beforeAndAfterPuzzles(self, phrases):
        if not phrases:
            return []
        res = set()
        start_word = defaultdict(list)
        for i,phrase in enumerate(phrases):
            words = phrase.split()
            start_word[words[0]].append(i)

        for i,phrase in enumerate(phrases):
            words = phrase.split()
            last_word = words[-1]
            # act as before phrase
            if last_word in start_word:
                for j in start_word[last_word]:
                    if i == j:
                        continue
                    new_phrase = words + phrases[j].split()[1:]
                    string = ' '.join(new_phrase)
                    res.add(string)
        new_list = list(res)
        new_list.sort()
        return new_list
sol = Solution()
arr = ["ueoogqi fd chcr pkwllylq zbcogrmp jghkvf sgtz","xtuezwre zbcogrmp a doykajxm fqax eymf po jghkvf aztdai jghkvf mxl gdyxo qfaidrh x","fd mxl shymouv cpwvq prmcvnoc nzxr p u p","xdqbhgtt fd efof rv lfhga x","mtb aztdai bpl pb","jhusu","c pkwllylq jinepsy prmcvnoc iq po gshnu baqs klg pxfuvk","prmcvnoc nzxr pkwllylq jghkvf rv sgtz chcr aztdai gdyxo gmp vgdzz gdyxo nzxr vw","hzpmuewr jghkvf gwgzpz rmtpuggu jibcudb p yi jghkvf prmcvnoc ki yi cudx","po dpk j up gdyxo zrumhwf akbei mtkmkcue xwuscivt prmcvnoc gmp fd eymf rv p","rmtpuggu yi w ej po chcr nvldffol nzxr dpk rv u prmcvnoc","u an","c xdqbhgtt prmcvnoc clwvt j akbei sukfgn xfqm vw efof jghkvf sukfgn pkwllylq cudx bpl cpwvq x","zrumhwf gdhh efof prmcvnoc brfvbhf bhkr dbehcm scqcnfsr xwuscivt rtx yi p fd scqcnfsr gmp b gzxdff","gwgzpz vw scqcnfsr mtkmkcue ueoogqi gbub clwvt mtb xvsrwqzh lfhga xdqbhgtt fqhk sukfgn p a","vw gdypilwq dbidurjo vrjk up jghkvf lr pxfuvk doykajxm iwynwx vw","akbei nsrxtp dbehcm c","nsrxtp nvldffol jibcudb lr xfqm pkwllylq t cudx xvsrwqzh yi","eymf x a","gmp an jibcudb vgdzz aztdai gdypilwq efof zsloxyq shymouv yi prmcvnoc sgtz t","rtx pb mtkmkcue dbehcm efof shymouv ki baqs ueoogqi qdzccepw cudx gzxdff fd","wofisjc pb w nsrxtp o c j klg","gzxdff efof x","fqax xtuezwre qdzccepw dbidurjo rv jhusu jghkvf jinepsy mxl","iq mtb shymouv bxfsx kktr nzxr pnwi x","qfaidrh po jinepsy sukfgn iq hdhsaghq tvmlodx dpk gdyxo dbehcm kktr qdzccepw wgpxvxkk","akbei xwuscivt p ki oixssao lfhga pxfuvk","shymouv p klg vw xdqbhgtt lhaj baqs rv qfaidrh t kktr uboro o zbcogrmp rmtpuggu yi vw c","gshnu vgse xvsrwqzh b jghkvf yi shymouv w zmw ki xwuscivt klg","vw tvmlodx prmcvnoc uboro an","dbidurjo klg t w","x","u dpk aztdai jghkvf vrjk up x lr efof prmcvnoc x","jhusu sgtz tvmlodx clwvt dpk iwynwx b gshnu xtuezwre eveqtuz qdzccepw gdhh zbcogrmp x lr p fqhk o b","nvldffol tvmlodx rtx","oixssao jibcudb bhkr fqax x mtb mtkmkcue wgpxvxkk ki po w","iwynwx","w a","cpwvq","ueoogqi o lhaj","xdqbhgtt b bxfsx zrumhwf an hzpmuewr lr bpl gdypilwq b u","pb u wgpxvxkk xtuezwre ki gdyxo wgpxvxkk qdzccepw p jibcudb mtb","fqax zbcogrmp bhkr cudx an mxl cpwvq aztdai gmp","jinepsy zbcogrmp akbei cpwvq doykajxm zmw rtx","lr gzxdff zmw efof eveqtuz hzpmuewr o","j xtuezwre pxfuvk aztdai","po zrumhwf lr gbub eveqtuz jinepsy a","lhaj","fqax yi hzpmuewr mtkmkcue scqcnfsr fd doykajxm bhkr scqcnfsr","gzxdff ueoogqi zrumhwf gdypilwq brfvbhf brfvbhf t t","lfhga xwuscivt x rtx po lhaj akbei lhaj dbidurjo t pnwi","p mtkmkcue baqs","vgdzz ueoogqi xdqbhgtt gdyxo dpk b","vrjk rmtpuggu cpwvq tvmlodx gwgzpz lhaj j","xvsrwqzh gshnu klg bhkr qfaidrh jinepsy vgdzz mtb ki zmw sukfgn akbei p bhkr rtx mtkmkcue j","rtx jibcudb gdhh hzpmuewr zbcogrmp iwynwx","aztdai zrumhwf zsloxyq kktr scqcnfsr pkwllylq t","akbei chcr p xfqm lhaj vw hdhsaghq scqcnfsr ki chcr zmw cpwvq an fqhk","x zmw lr","sgtz x lhaj x jinepsy p","dbidurjo oixssao","rmtpuggu xdqbhgtt vrjk baqs o hzpmuewr x j qfaidrh gwgzpz pxfuvk xtuezwre an x","gnuugpoi zrumhwf hdhsaghq clwvt sukfgn j zrumhwf up gmp","t eymf vw iwynwx sukfgn mxl qfaidrh yi mtb baqs hzpmuewr klg","zmw gnuugpoi scqcnfsr x gdyxo","rtx lhaj vw a fqax u chcr gnuugpoi p baqs pkwllylq","o dpk po x gzxdff dpk b","jghkvf zrumhwf vgdzz jhusu vrjk jhusu vw aztdai rv gdypilwq po gmp cpwvq xvsrwqzh dpk up a gwgzpz j","zrumhwf doykajxm ki baqs iq efof a mxl qdzccepw clwvt vgse cudx xfqm wofisjc up yi xfqm cudx vrjk o","jinepsy dbidurjo efof fd brfvbhf xwuscivt gdypilwq nsrxtp lr wgpxvxkk gbub a","hdhsaghq x a scqcnfsr chcr pb qdzccepw o","hzpmuewr an x dbehcm aztdai j pnwi ki","gdhh gnuugpoi yi ej kktr gbub gnuugpoi gdhh xvsrwqzh doykajxm sukfgn x zmw","nzxr gdhh wgpxvxkk akbei tvmlodx po mtb hzpmuewr baqs shymouv bxfsx gshnu","gmp sukfgn shymouv iwynwx hdhsaghq scqcnfsr efof tvmlodx kktr xvsrwqzh x vw aztdai gmp up","t","iq an mtkmkcue pnwi gwgzpz xtuezwre jghkvf gbub oixssao rv c lr a dpk ki","xtuezwre mtb","gwgzpz","zbcogrmp zbcogrmp vgdzz gdypilwq nsrxtp mtkmkcue jinepsy pkwllylq po uboro bhkr gdyxo gmp ki fqhk","o hdhsaghq vw lhaj clwvt xdqbhgtt eymf xtuezwre","cpwvq vrjk kktr bxfsx pnwi wofisjc lfhga x","fd gdhh xtuezwre","jhusu","jibcudb bpl gdyxo fd lhaj lfhga jhusu","nzxr qdzccepw up gdhh fd jhusu u p vw","rmtpuggu zbcogrmp gshnu bxfsx xwuscivt a an fqax u fqax qfaidrh c o","zbcogrmp iq gwgzpz dbidurjo aztdai mxl zsloxyq gdyxo up gdyxo w fd ki p x baqs zrumhwf hzpmuewr p","eveqtuz an doykajxm w vw a","zbcogrmp t w","gbub xvsrwqzh a","lhaj pnwi ki zmw b mtkmkcue cudx ueoogqi cudx rtx brfvbhf cpwvq an fd","wofisjc","pb vw","lhaj vrjk fd bhkr o","iq iwynwx clwvt o nsrxtp rmtpuggu baqs rtx x x","u j c","baqs jghkvf aztdai j tvmlodx jinepsy up","nvldffol dpk sgtz","mtb vgse chcr"]
print(sol.beforeAndAfterPuzzles(arr))
# ["a chip off the old block party",
#          "a man on a mission impossible",
#          "a man on a mission statement",
#          "a quick bite to eat my words",
#          "chocolate bar of soap"]
# #print(sol.beforeAndAfterPuzzles(phrases = ["mission statement",
#                   "a quick bite to eat",
#                   "a chip off the old block",
#                   "chocolate bar",
#                   "mission impossible",
#                   "a man on a mission",
#                   "block party",
#                   "eat my words",
#                   "bar of soap"]))
# print(sol.beforeAndAfterPuzzles(["writing code","code rocks"]))


