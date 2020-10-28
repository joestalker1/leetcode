class Solution:
    def removeDuplicates(self, S: str):
        res = []
        last_pos = {}
        for i in range(len(S)):
            ch = S[i]
            if res and res[-1] == ch:
                last_pos[ch] = -1
                res.pop()
                continue
            else:
                res.append(ch)
                last_pos[ch] = i
        return ''.join(res)


sol = Solution()
print(sol.removeDuplicates("aaaa"))
print(sol.removeDuplicates("abbaca"))
print(sol.removeDuplicates("azxxzy"))



