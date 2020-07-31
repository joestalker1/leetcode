class Solution:
    def lengthLongestPath(self, input: str) -> int:

        inp = input.split("\n")
        stack = []  # will contain (dirname, level)
        op = [0]  # for empty result like "a"
        for tm in inp:
            subs = tm.split('\t')
            c = len(subs)
            last = subs[-1]
            if c == 1 and last[:4] == '    ':
                last = last[4:]
            else:
                while stack and stack[-1][1] >= c:
                    stack.pop()
                if '.' in last:
                    tmp = ''
                    for k in stack:
                        tmp += '/' + k[0]
                    tmp += last
                    op.append(len(tmp))
                else:
                    stack.append([last, c])
        return max(op)


sol = Solution()
#print(sol.lengthLongestPath("dir\n    file.txt"))
print(sol.lengthLongestPath("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"))#20
