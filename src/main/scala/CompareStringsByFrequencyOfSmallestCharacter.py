import bisect

class Solution:
    def numSmallerByFrequency(self, queries, words):
        def freq(s):
            if len(s) == 0:
                return 0
            ch = min(list(s))
            count = 0
            for c in s:
                if c == ch:
                    count+=1
            return count
        word_freq = [freq(w) for w in words]
        word_freq.sort()
        ans = []
        for query in queries:
            f = freq(query)
            i = bisect.bisect_right(word_freq, f)
            ans.append(len(word_freq) - i)
        return ans


sol = Solution()
print(sol.numSmallerByFrequency(["cbd"], ["zaaaz"]))








