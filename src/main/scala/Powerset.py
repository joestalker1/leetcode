def powerset(nums):

    def get_power_set(start, res, buf):
        if buf:
            res.append(buf[::])
        for i in range(start, len(nums)):
            buf.append(nums[i])
            get_power_set(i+1, res, buf)
            buf.pop()

    res = []
    get_power_set(0, res, [])
    return res

print(powerset([1,2,3]))