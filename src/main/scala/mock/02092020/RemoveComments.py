class Solution:
    def removeComments(self, source):
        if not source:
            return ""

        res = []
        i = 0
        while i < len(source):
            s = source[i]
            c1 = s.find('//')
            c2 = s.find('/*')
            if c1 < c2 and c1 != -1:
                sub = s[:i]
                if sub:
                    res.append(sub)
                i += 1
            elif c1 > c2 and c2 != -1:
                #skip all string until it'' equal */
                j = i
                c1 = s.find('*/', c2 + 2)
                while j < len(source) and c1 == -1:
                    j += 1
                    c1 = s.find('*/')
                sub = s[c1 + 2:]
                if sub:
                    res[-1] += sub
                i = j + 1
            else:
                res.append(s)
                i += 1
        return res


sol = Solution()
print(sol.removeComments(["struct Node{", "    /*/ declare members;/**/", "    int size;", "    /**/int val;", "};"]))
print(sol.removeComments(
    ["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test",
     "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]))
