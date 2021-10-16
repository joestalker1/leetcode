class Solution:
    def minOperationsToFlip(self, exp: str) -> int:
        d = {}

        def brackets(s, d):
            st = []
            for i,ch in enumerate(exp):
                if ch == '(':
                    st.append(i)
                elif ch == ')':
                    d[i] = st.pop()

        def dfs(s, e, d):
            if s == e:
                return[int(exp[s]), 1]
            # check if it's another bracket
            s2 = d.get(e, e)
            if s2 == s:
                return dfs(s + 1,e - 1, d)
            p1,c1 = dfs(s, s2-2,d)
            p2,c2 = dfs(s2, e,d)
            op = exp[s2 - 1]
            t = {'|': lambda x,y:x|y, '&': lambda x,y: x & y}
            c3 = 1 if p1 + p2 == 1 else min(c1, c2) + (p1 ^ (op == "&"))
            return [t[op](p1,p2), c3]

        brackets(exp, d)
        return dfs(0,len(exp) - 1, d)[1]


sol = Solution()
print(sol.minOperationsToFlip("(0|0)&0"))#2



