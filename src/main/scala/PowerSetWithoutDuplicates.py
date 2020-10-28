def powerset_without_dup(nums):

    def get_power_set(start, res, buf):
        if buf:
            res.append(buf[::])
        for i in range(start, len(nums)):
            if i > start and nums[i-1] == nums[i]:
                continue
            buf.append(nums[i])
            get_power_set(i+1, res, buf)
            buf.pop()

    res = []
    nums.sort()
    get_power_set(0, res, [])
    return res

print(powerset_without_dup([1,1,2,3,2,4]))