def subsets(arr):
    arr.sort()

    def gen_subsets(start, res, temp):
        res.append(temp[::])
        for i in range(start, len(arr)):
            temp.append(arr[i])
            gen_subsets(i+1, res, temp)
            temp.pop(-1)
    res = []
    gen_subsets(0, res, [])
    return res

#without duplicates

def subsets2(arr):
    arr.sort()

    def backtrack(start, res, temp):
        res.append(temp[::])
        for i in range(start, len(arr)):
            if i > start and arr[i] == arr[i-1]:
                continue
            temp.append(arr[i])
            backtrack(i+1, res, temp)
            temp.pop(-1)
    res = []
    backtrack(0, res, [])
    return res

print(subsets2([1,1,2,2,3]))
print(subsets([1,1,2,2,3]))
#print(subsets([1,3,4,5]))

