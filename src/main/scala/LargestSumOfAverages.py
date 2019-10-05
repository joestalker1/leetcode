class Solution:
    def largestSumOfAverages1(self, A, K):
        if not A or K == 0:
            return 0

        def parition(pos, group, mem):
            if pos == len(A):
                if group == K:
                    return 0
                return float('-inf')
            if group == K:
                return float('-inf')
            if (pos, group) in mem:
                return mem[(pos, group)]
            max_sum = 0
            for right in range(pos, len(A)):
                part_sum = float(sum(A[pos: right + 1])) / (right - pos + 1)
                group_sum = part_sum + parition(right + 1, group + 1, mem)
                max_sum = max(max_sum, group_sum)
            mem[(pos, group)] = max_sum
            return max_sum

        return parition(0, 0, {})

    def largestSumOfAverages(self, A, K):
        if not A or K == 0:
            return 0

        average = [0] * (K + 1)
        for i in range(len(average)):
            average[i] = [0] * len(A)

        group_index = [0] * (K + 1)
        for i in range(len(group_index)):
            group_index[i] = [0] * len(A)
        #s[i,j] = s[j+1] - s[i]
        sum_arr = [0] * (len(A) + 1)
        for i in range(len(A)):
            sum_arr[i + 1] = sum_arr[i] + A[i]

        for i,a in enumerate(A):
            group_index[1][i] = i
            average[1][i] = float(sum_arr[i + 1] - sum_arr[0]) / (i + 1)
        for k in range(2, K + 1):
            for j in range(1, len(A)):
                i2 = group_index[k][j-1]
                if k + 1 <= K:
                    avg_new_group = average[k - 1][j - 1] + A[j] # start new group
                else:
                    avg_new_group = 0
                s = j - i2 - 1
                avg_same_group = float(sum_arr[j + 1] - sum_arr[s]) / (j - s + 1)  # add to the same group
                if avg_new_group > avg_same_group:
                    group_index[k][j] = 0
                    average[k][j] = avg_new_group
                else:
                    group_index[k][j] = i2 + 1
                    average[k][j] = avg_same_group
        return average[K][len(A) - 1]

sol = Solution()
#print(sol.largestSumOfAverages([7959,4983,5994,4877,705,3404,472,3700,2677,5242,3011,2077,9160,4218,3456,176,3425,2669,6622,4808], 19))
#print(sol.largestSumOfAverages([1], 1))
#print(sol.largestSumOfAverages([4,1,7,5,6,2,3], 4))
#print(sol.largestSumOfAverages([1,2,3,4,5,6,7], 4))
print(sol.largestSumOfAverages([9,1,2,3,9], 3))










