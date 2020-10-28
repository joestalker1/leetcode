class Solution:
    def expand(self, S):
        if not S:
            return []
        terms = S.split('}')
        terms = [t.split('{') for t in terms]
        if len(terms) == 1:
            return [S]
        n_tersm = []
        for t in terms:
            if len(t) == 0:
                continue
            for a in t:
                if len(a):
                    n_tersm.append(a)
        terms = n_tersm
        max_len = 1
        chars = []
        for term in terms:
            arr = term.split(',')
            max_len = max(max_len, len(arr))
            chars.extend([arr])
        res = []
        for i in range(len(chars[0])):
            res.append([chars[0][i]])

        for t in chars[1:]:
            new_res = []
            for ch in t:
                for s in res:
                    ns = s[::]
                    ns.append(ch)
                    new_res.append(ns)
            res = new_res
        return [''.join(arr) for arr in res]


sol = Solution()
print(sol.expand("abcd"))
print(sol.expand("{a,b,c}d{e,f}"))




