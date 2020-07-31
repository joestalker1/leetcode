from collections import defaultdict
import re

class Solution:
    def lengthLongestPath(self, input):
        if not input:
            return 0
        s = input.replace('\t', ' ')

        def dfs(s, pos, t):
            if pos == len(s):
                return 0
            #count space at
            sp = 0
            while pos < len(s) and s[pos]==' ':
                pos += 1
                sp += 1
            max_len = 0
            if sp == t:
                # the same level

