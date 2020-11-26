def combination(arr, k):
    ans = []

    def comb(ans, path, options, count):
        if count == 0:
            ans.append(path)
            return
        for i, a in enumerate(options):
            comb(ans, path + [a], options[i + 1:], count - 1)

    comb(ans, [], arr, k)
    return ans


print(combination([1, 2, 3, 4], 5))
