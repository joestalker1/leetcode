class Solution:
    def maximizeSweetness(self, sweetness, K: int):
        #min sweetness is sweetness of one chunk
        lo = min(sweetness)
        #max is total sum of all chunks
        hi = sum(sweetness)

        def count_pieces(min_piece):
            #count if every piece may be not less than min_piece
            cur_sweet = 0
            c = 0
            for i in range(len(sweetness)):
                cur_sweet += sweetness[i]
                if cur_sweet >= min_piece:
                    c += 1
                    cur_sweet = 0
            return c
        # increment for me
        K += 1
        #find max of min sweetness
        while lo <= hi:
            m = lo + (hi - lo) // 2
            # if we can't split for K persons, then reduce min_sweetness
            if count_pieces(m) < K:
                hi = m - 1
            else:
                #otherwise increase it
                lo = m + 1
        # here is not obvious but we return hi as min(lo,hi) in the end.
        return hi

sol = Solution()
print(sol.maximizeSweetness([1,2,2,1,2,2,1,2,2], 2))#5
print(sol.maximizeSweetness([5,6,7,8,9,1,2,3,4], 8))#1
print(sol.maximizeSweetness([1,2,3,4,5,6,7,8,9], 5))#6