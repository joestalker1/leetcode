class Solution:
    def confusingNumberII(self, N):
        nums = [0, 1, 6, 8, 9]
        rotation = [0, 1, -1, -1, -1, -1, 9, -1, 8, 6]
        count = [0]

        def to_num(arr):
            s = 0
            base = 1
            for i in range(len(arr)-1,-1,-1):
                s += base * arr[i]
                base *= 10
            return s

        def is_valid(a):
            b = a
            res = 0
            while b > 0:
                n = b % 10
                res = res * 10 + rotation[n]
                b = b // 10
            return a != res

        def get_confusing_num(buf, count):
            if buf:
                #print(buf)
                a = to_num(buf)
                if a == 0 or a > N:
                    return
                if is_valid(a):
                    count[0] += 1
                if a * 10 > N:
                    return
            for i in range(len(nums)):
                buf.append(nums[i])
                get_confusing_num(buf, count)
                buf.pop()
        get_confusing_num([], count)
        return count[0]


sol = Solution()
print(sol.confusingNumberII(1000000000))
print(sol.confusingNumberII(100))
print(sol.confusingNumberII(20))#6



