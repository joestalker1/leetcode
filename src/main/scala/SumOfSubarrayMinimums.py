class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        MOD = 10 ** 9 + 7
        res = 0 # min arrays sum
        dot = 0
        st = [] #(min_val, count) = run length encoding, count of min_val in arrays
        #consider arrrays with min_vals: 0:i,1:i, 2:i and so on
        for i,a in enumerate(A):
            #array is from one [a]
            count = 1
            # pop old greater min_val arrays, replace it by new min_val - a
            while st and st[-1][0] >= a:
                x,c = st.pop()
                # count new arrays min
                count += c
                #subtract old min sums
                dot -= x*c
            #get count array with min a
            st.append([a, count])
            dot += a * count
            res += dot
        return res % MOD