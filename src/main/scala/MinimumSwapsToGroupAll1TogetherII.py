class Solution:
    def makeSubKSumEqual(self, arr, k: int) -> int:
        n = len(arr)
        gcd = math.gcd(n, k)
        min_op = 0
        for i in range(gcd):
            temp = [arr[j] for j in range(i, n, gcd)]
            temp.sort()
            median = temp[len(temp) // 2]
            min_op += sum(abs(a - median) for a in temp)
        return min_op

