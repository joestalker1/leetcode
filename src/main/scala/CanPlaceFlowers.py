class Solution:
    def canPlaceFlowers(self, flowerbed, n: int) -> bool:
        return self._canPlaceFlowers(flowerbed, n)

    def _canPlaceFlowers(self, flowerbed, n: int) -> bool:
        planted_cnt = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                continue
            empty_left = (i == 0) or (flowerbed[i - 1] == 0)
            empty_right = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
            if empty_left and empty_right:
                flowerbed[i] = 1
                planted_cnt += 1
                if planted_cnt >= n:
                    return True
        return planted_cnt >= n