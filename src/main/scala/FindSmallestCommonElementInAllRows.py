class Solution:
    def smallestCommonElement(self, mat) -> int:
        if not mat:
            return 0
        for i in range(len(mat[0])):
            matched = True
            for j in range(1,len(mat)):
                k = bisect.bisect_left(mat[j], mat[0][i])
                if k == len(mat[j]):
                    return -1
                if mat[j][k] != mat[0][i]:
                    matched = False
                    break
            if matched:
                return mat[0][i]
        return -1