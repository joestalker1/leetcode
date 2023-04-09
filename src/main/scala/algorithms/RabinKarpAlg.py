class Solution:
    def fuzzysearch(self, s, substr):
        if not s and not substr:
            return True
        if not s or not substr or len(s) < len(substr):
            return False

        def find(idx_in_s, idx_in_substr):
            if idx_in_substr == len(substr):
                # if we reach the end of substring, we can return True
                return True
            if idx_in_s == len(s):
                # if we reach the end of string, we check if we reach end of substring
                return idx_in_substr == len(substr)
            if s[idx_in_s] == substr[idx_in_substr]:
                # if chars matches, we have 2 options: go to the next char in string or we stay on the same char
                return find(idx_in_s + 1, idx_in_substr+1) or find(idx_in_s, idx_in_substr + 1)
            #increment next string char
            return find(idx_in_s+1, idx_in_substr)

        return find(0, 0)


    def fuzzysearch2(self, s, substr):
        if not s and not substr:
            return True
        if not s or not substr:
            return False

        d = 256
        q = 10**9 + 7
        m = len(substr)
        n = len(s)
        hash_for_substr = 0
        hash_for_s = 0
        h = 1
        #pow_of_d(d, m - 1) % q
        for i in range(m - 1):
            h = (h * d) % q
        for i in range(m):
            hash_for_substr = (hash_for_substr * d + ord(substr[i])) % q
            hash_for_s = (hash_for_s * d + ord(s[i])) % q
        for i in range(n - m + 1):
            if hash_for_substr == hash_for_s:
                for j in range(m):
                    if s[i+j] != substr[j]:
                        break
                    else:
                        j += 1
                if j == m:
                    return True
            if i < n - m:
                hash_for_s = (d * h * (hash_for_s - ord(substr[i])) + ord(substr[i+m])) % q
                if hash_for_s < 0:
                    hash_for_s += q
        return True

# uzzysearch("catw", "catwheel") == true
# fuzzysearch("cat", "catwheel") == true
# fuzzysearch("ctw", "catwheel") == true
# fuzzysearch("lw", "catwheel") == false
# fuzzysearch("tw", "catwheel") == true


sol = Solution()
assert sol.fuzzysearch("aaaaaaaaaaaaaaaaaaaaaaaaaabadsasadasdjadjahjhsdhsjdjssjhdjhjshdjsjdsjdhjsdhjshdjshjdhjaaaaaaaaaaaaaaaaaaaaaaaaaabadsasadasdjadjahjhsdhsjdjssjhdjhjshdjsjdsjdhjsdhjshdjshjdhjscatwheelcatwheelcatwheel","catw"), 'test1'
assert sol.fuzzysearch("aaaaaaaaaaaaaaaaaaaaaaaaaabadsasadasdjadjahjhsdhsjdjssjhdjhjshdjsjdsjdhjsdhjshdjshjdhjaaaaaaaaaaaaaaaaaaaaaaaaaabadsasadasdjadjahjhsdhsjdjssjhdjhjshdjsjdsjdhjsdhjshdjshjdhjcatwheelcatwheelcatwheel", "cat"), 'test2'
assert sol.fuzzysearch("aaaaaaaaaaaaaaaaaaaaaaaaaabadsasadasdjadjahjhsdhsjdjssjhdjhjshdjsjdsjdhjsdhjshdjshjdhjaaaaaaaaaaaaaaaaaaaaaaaaaabadsasadasdjadjahjhsdhsjdjssjhdjhjshdjsjdsjdhjsdhjshdjshjdhjcatwheelcatwheelcatwheel", "ctw"), 'test3'
assert sol.fuzzysearch("aaaaaaaaaaaaaaaaaaaaaaaaaabadsasadasdjadjahjhsdhsjdjssjhdjhjshdjsjdsjdhjsdhjshdjshjdhjaaaaaaaaaaaaaaaaaaaaaaaaaabadsasadasdjadjahjhsdhsjdjssjhdjhjshdjsjdsjdhjsdhjshdjshjdhjcatwheelcatwheelcatwheel", "lw"), 'test4'
assert sol.fuzzysearch("aaaaaaaaaaaaaaaaaaaaaaaaaabadsasadasdjadjahjhsdhsjdjssjhdjhjshdjsjdsjdhjsdhjshdjshjdhjaaaaaaaaaaaaaaaaaaaaaaaaaabadsasadasdjadjahjhsdhsjdjssjhdjhjshdjsjdsjdhjsdhjshdjshjdhjcatwheelcatwheelcatwheel", "tw"), 'test5'
assert sol.fuzzysearch("aaaaaaaaaaaaaaaaaaaaaaaaaabadsasadasdjadjahjhsdhsjdjssjhdjhjshdjsjdsjdhjsdhjshdjshjdhjaaaaaaaaaaaaaaaaaaaaaaaaaabadsasadasdjadjahjhsdhsjdjssjhdjhjshdjsjdsjdhjsdhjshdjshjdhjaaaaaaaaaaaaaaaaaaaaaaaaaabadsasadasdjadjahjhsdhsjdjssjhdjhjshdjsjdsjdhjsdhjshdjshjdhjcatwheelcatwheelcatwheel", "cot") == False, 'test5'




