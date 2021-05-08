class Solution:
    def countRangeSum(self, nums, lower, upper):
        n = len(nums)
        pr = [0] * n
        pr[0] = nums[0]
        for i in range(1, n):
            pr[i] = pr[i-1] + nums[i]
        pr = [0] + pr
        #we merge and sort prefix sum
        # r is exclusive
        def mergeSort(pr, s, e):
            if (e - s) <= 1:
                return 0
            mid = s + (e - s) //2
            count = mergeSort(pr, s, mid) + mergeSort(pr, mid, e)
            # we look at second half
            k = mid # from pr[k] - pr[i] >= lower
            j = mid # pr[j] - pr[i] < upper
            t = mid
            r = 0
            cache = [0] * (e - s)
            for i in range(s, mid):
                #consider [i,k,j) subarray
                while k < e and (pr[k] - pr[i]) < lower:
                    k += 1
                while j < e and (pr[j] - pr[i]) <= upper:
                    j += 1
                # put into cache pr[t]< pr[i]
                while t < e and pr[i] > pr[t]:
                    cache[r] = pr[t]
                    t += 1
                    r += 1
                cache[r] = pr[i]
                count += (j - k)
                r += 1
            #put to pr sorted values
            j = s
            for i in range(t - s):
                pr[j] = cache[i]
                j += 1
                i += 1
            return count
        return mergeSort(pr, 0, len(pr))


sol = Solution()
print(sol.countRangeSum([2147483647,-2147483648,-1,0],-1,0))#4
print(sol.countRangeSum([1,1,1,1],1,4))#3
print(sol.countRangeSum([-2,5,-1], -2, 2))#3

