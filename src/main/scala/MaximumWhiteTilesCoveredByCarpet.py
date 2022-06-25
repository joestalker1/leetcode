import bisect

class Solution:
    def maximumWhiteTiles(self, tiles, carpetLen: int) -> int:
        # connect adjacent tiles
        tiles.sort(key=lambda x: x[0])
        pr = [0] * (len(tiles)+1)
        start_pos = [tiles[i][0] for i in range(len(tiles))]
        for i in range(1, len(tiles)+1):
            pr[i] = pr[i-1] + tiles[i-1][1] - tiles[i-1][0] + 1
        max_len = 0
        for i in range(len(tiles)):
            s = tiles[i][0]
            end_carp = s + carpetLen - 1
            if end_carp <= tiles[i][1]:
                return carpetLen
            j = bisect.bisect_right(start_pos, end_carp) - 1
            comp = 0
            if tiles[j][1] > end_carp:
                comp = tiles[j][1] - end_carp
            max_len = max(max_len, pr[j+1] - pr[i] - comp)
        return max_len


sol = Solution()
print(sol.maximumWhiteTiles([[10,11],[1,1]],2))#2
print(sol.maximumWhiteTiles([[1,5],[10,11],[12,18],[20,25],[30,32]],10))#9