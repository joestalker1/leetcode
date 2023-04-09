import bisect

class Solution:
    def kIncreasing(self, arr, k: int) -> int:
        if not arr:
            return 0
        # 6 -3 = 3: 0,3; 1,4; 2,5, 3
        # [4,1,5,2,6,2], k = 3
        #[1,2,3,1,2,3]
        def longest_inc_subseq(arr):
            sub = []
            for i in range(len(arr)):
                if not sub or sub[-1] <= arr[i]:
                    sub.append(arr[i])
                else:
                    s = bisect.bisect_right(sub, arr[i])
                    sub[s] = arr[i]
            return len(sub)

        min_op = 0
        for i in range(k):
            sub_seq = []
            for j in range(i, len(arr),k):
                sub_seq.append(arr[j])
            min_op += len(sub_seq) - longest_inc_subseq(sub_seq)
        return min_op