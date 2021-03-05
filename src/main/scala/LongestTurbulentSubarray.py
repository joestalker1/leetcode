class Solution:
    def maxTurbulenceSize(self, arr):
        if len(arr) <= 1:
            return len(arr)
        max_len = 0
        last_num = -1
        last_rel = -1 #0 is less, 1 is greater
        cur_len = 0
        for i in range(len(arr)):
            if cur_len == -1:
                cur_len = 1
                last_num = arr[i]
            else:
                if last_num == arr[i]:
                    last_rel = -1
                    cur_len = 1
                    last_num = arr[i]
                elif last_rel == 1 and last_num > arr[i] or last_rel == 0 and last_num < arr[i]:
                    cur_len = 2
                    last_rel = 1 if last_num > arr[i] else 0
                    last_num = arr[i]
                else:
                    cur_len += 1
                    last_rel = 1 if last_num > arr[i] else 0
                    last_num = arr[i]
            max_len = max(max_len, cur_len)
        return max_len


sol = Solution()
print(sol.maxTurbulenceSize([111]))
print(sol.maxTurbulenceSize([4,8,12,16]))#2
print(sol.maxTurbulenceSize([9,4,2,10,7,8,8,1,9]))#5

