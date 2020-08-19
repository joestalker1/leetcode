class Solution:
    def addBoldTag(self, s: str, dict):
        if not s:
            return None
        ranges = []

        for word in dict:
            i = s.find(word)
            if i == -1:
                continue
            while i != -1 and i < len(s):
                j = i + len(word)
                ranges.append([i, j])
                i = s.find(word, j)

        ranges.sort(key=lambda x: x[0])

        # try merge last range and new one
        new_ranges = []
        for r in ranges:
            if len(new_ranges) > 0 and r[0] <= new_ranges[-1][1]:
                new_ranges[-1][1] = max(r[1], new_ranges[-1][1])
            else:
                new_ranges.append(r)

        res = []

        start = 0
        for s1, e1 in new_ranges:
            end = s1
            res.append(s[start:end])
            res.append(f"<b>{s[s1:e1]}</b>")
            start = e1
        res.append(s[start:])
        return ''.join(res)


sol = Solution()
print(sol.addBoldTag("aaabbcc",["aaa","aab","bc"]))
print(sol.addBoldTag("aaabbcc", ["a","b","c"]))
print(sol.addBoldTag(
    "qrzjsorbkmyzzzvoqxefvxkcwtpkhzbakuufbpgdkykmojwuennrjeciqvvacpzrrczfhxnsmginzwinzihpomxtmweyyzzmgcoiupjnidphvzlnxtcogufozlenjfvokztghwckzyvmktduqkizixzxpanjwrdeudjyftxksjgdklwxrhmudhrtemuvelykqaafzlqmennttkighcdxfozdcoqkyshhajipnsdrljrnlwmyjuwxsebpqm",
    ["qr", "zj", "so", "rb", "km", "yz", "zz", "vo", "qx", "ef", "vx", "kc", "wt", "pk"]))
#"<b>qrzjsorbkmyzzzvoqxefvxkcwtpk</b>hzbakuufbpgdky<b>km</b>ojwuennrjeciqvvacpzrrczfhxnsmginzwinzihpomxtmwey<b>yzz</b>mgcoiupjnidphvzlnxtcogufozlenjf<b>vo</b>kztghwckzyvmktduqkizixzxpanjwrdeudjyftxksjgdklwxrhmudhrtemuvelykqaafzlqmennttkighcdxfozdcoqkyshhajipnsdrljrnlwmyjuwxsebpqm"
#my result is
#<b>qrzjsorbkmyzz</b>z<b>voqxefvxkcwtpk</b>hzbakuufbpgdky<b>km</b>ojwuennrjeciqvvacpzrrczfhxnsmginzwinzihpomxtmwey<b>yzz</b>mgcoiupjnidphvzlnxtcogufozlenjf<b>vo</b>kztghwckzyvmktduqkizixzxpanjwrdeudjyftxksjgdklwxrhmudhrtemuvelykqaafzlqmennttkighcdxfozdcoqkyshhajipnsdrljrnlwmyjuwxsebpqm


