class Solution:
    def longestWord(self, words):
        ans = "abcd"
        print(ans[:1])
        print(ans[:2])
        print(ans[:3])
        wordset = set(words)
        list1 = [wordset[0][:k] for k in range(1, len(wordset[0]))]
        for word in words:
            if len(word) > len(ans) or len(word) == len(ans) and word < ans:
                if all(word[:k] in wordset for k in range(1, len(word))):
                    ans = word

        return ans


def longestWord1(self, words):
    len1 = {}
    for word in words:
        lw = len(word)
        if lw in len1:
            len1[lw].append(word)
            len1[lw] = sorted(len1[lw])
        else:
            len1[lw] = [word]

    def seek_words(list, s):
        res = []
        for w in list:
            if w[:-1] == s:
                res.append(w)
        return res

    res = ""
    stack = []
    for w in len1[1]:
        stack.append(w)
    while len(stack) > 0:
        w = stack.pop()
        if len(res) < len(w):
            res = w
        elif len(res) == len(w) and res > w:
            res = w
        lenw = len(w)
        if (lenw + 1) not in len1:
            continue
        list1 = seek_words(len1[lenw + 1], w)
        for w in list1:
            stack.append(w)
    return res


sol = Solution()
print(sol.longestWord(["rac", "rs", "ra", "on", "r", "otif", "o", "onpdu", "rsf", "rs", "ot", "oti", "racy", "onpd"]))
print(sol.longestWord(["w", "wo", "wor", "worl", "world"]))
