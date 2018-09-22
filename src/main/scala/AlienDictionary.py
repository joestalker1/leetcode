import collections
class Solution:
    def alienOrder(self, words):
        pre = collections.defaultdict(set)
        suc = collections.defaultdict(set)

        for pair in zip(words, words[1:]):
            for a, b in zip(*pair):
                if a != b:
                    suc[a].add(b)
                    pre[b].add(a)
                    break
        chars = set(''.join(words))
        #get first char without predecesesor
        charToProcess = chars - set(pre)
        order = ''
        while charToProcess:
            ch = charToProcess.pop()
            order += ch
            for b in suc[ch]:
                pre[b].discard(ch)
                if not pre[b]: # if processed all predecesesors let's add curret char to charToProcess
                    charToProcess.add(b)
        return order * (set(order) == chars)

sol = Solution()
#print(sol.alienOrder(["zy","zx"])) #yxz
#print(sol.alienOrder(["z","z"]))
#print(sol.alienOrder(["z","x","z"]))
print(sol.alienOrder(["aac","aabb","aaba"]))
#"cba"
print(sol.alienOrder([
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]))