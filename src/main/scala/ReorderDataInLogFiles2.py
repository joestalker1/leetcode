class Solution:
    def reorderLogFiles(self, logs):
        if not logs:
            return []
        res = [[], []]
        for log in logs:
            arr =log.split(' ')
            if '0'<= arr[1][0] <= '9':
                res[1].append(log)
            else:
                res[0].append([arr[0], ' '.join(arr[1:])])
        def compar(x):
            k,s = x
            return [s,k]
        res[0].sort(key=compar)
        return [k+' '+ s for k,s in res[0]] + res[1]

sol = Solution()
print(sol.reorderLogFiles(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]))
print(sol.reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))