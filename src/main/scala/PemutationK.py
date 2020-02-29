def permutation(arr):
    ans = []

    def perm(ans, cur, options):
        if len(cur) == len(arr):
            ans.append(cur)
            return
        for i,a in enumerate(options):
            perm(ans,cur+[a], options[:i]+options[i+1:])

    perm(ans, [], arr)
    return ans

print(permutation([1,2,3,4]))