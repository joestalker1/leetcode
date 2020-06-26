class Solution:
    def calculate(self, s):
        if not s:
            return None

        def op_pr(op):
            if op == '*' or op == '/':
                return 1
            return 0

        def conv_to_rev_polish(s):
            out = []
            st = []
            i = 0
            while i < len(s):
                if s[i].isdigit():
                    a = ''
                    while i < len(s) and s[i].isdigit():
                        a += s[i]
                        i += 1
                    out.append(a)
                elif s[i] not in '*/+-':
                    i += 1
                    continue
                else:
                    while st and op_pr(st[-1]) >= op_pr(s[i]):
                        out.append(st.pop())
                    st.append(s[i])
                    i += 1
            while st:
                out.append(st.pop())
            return out

        pn = conv_to_rev_polish(s)
        st = []
        for v in pn:
            if v.isdigit():
                st.append(int(v))
            else:
                a, b = st.pop(), st.pop()  # keep operand oder
                if v == '*':
                    st.append(a * b)
                elif v == '/':
                    st.append(b // a)
                elif v == '-':
                    st.append(b - a)
                else:
                    st.append(a + b)
        return st[0]


sol = Solution()
print(sol.calculate(" 3+5 / 2 "))
print(sol.calculate("3+2*2"))
