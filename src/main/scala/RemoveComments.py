class Solution:
    def removeComments(self, source):
        res = []
        in_block = False
        for line in source:
            i = 0
            if not in_block:
                new_line = []
            while i < len(line):

                if line[i:i+2] == '/*' and not in_block:

                    in_block = True
                    i += 1
                elif line[i:i+2] == '*/' and in_block:
                    in_block = False
                    i += 1
                elif line[i:i+2] == '//' and not in_block:
                    break
                elif not in_block:
                    new_line.append(line[i])
                i += 1
            if new_line and not in_block:
                res.append(''.join(new_line))
        return res


sol = Solution()
print(sol.removeComments(["struct Node{", "    /*/ declare members;/**/", "    int size;", "    /**/int val;", "};"]))
print(sol.removeComments(
    ["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test",
     "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]))
