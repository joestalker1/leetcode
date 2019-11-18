def sort_stack(nums):
    if not nums:
        return
    temp = []
    while nums:
        t = nums.pop()
        while temp and temp[-1] > t:
            a = temp.pop()
            nums.append(a)
        temp.append(t)
    return temp

print(sort_stack([34, 3, 31, 98, 92, 23]))
