class Solution:
    def lengthLongestPath(self, input):
        maxlen = 0
        pathlen = {0: 0}
        for line in input.splitlines():
            name = line.lstrip('\t')
            depth = len(line) - len(name)
            if '.' in name:
                maxlen = max(maxlen, pathlen[depth] + len(name))
            else:
                # + 1 for /
                #ignore previous path on the same level
                pathlen[depth + 1] = pathlen[depth] + len(name) + 1
        return maxlen


sol = Solution()
#print(sol.lengthLongestPath("rzzmf\nv\n\tix\n\t\tiklav\n\t\t\ttqse\n\t\t\t\ttppzf\n\t\t\t\t\tzav\n\t\t\t\t\t\tkktei\n\t\t\t\t\t\t\thhmav\n\t\t\t\t\t\t\t\tbzvwf.txt"))#47
#print(sol.lengthLongestPath2("dir\n        file.txt"))#16
print(sol.lengthLongestPath("dir\n        file.txt"))#16
print(sol.lengthLongestPath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"))#32
print(sol.lengthLongestPath('dir.txt'))
print(sol.lengthLongestPath("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"))