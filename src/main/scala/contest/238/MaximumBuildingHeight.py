class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        if not restrictions:
            return n - 1
        restrictions.extend([[1, 0], [n, n - 1]])
        restrictions.sort(key=lambda x: x[0])

        def calc_height(lst):
            max_height = 0
            for i in range(1, len(lst)):
                h1 = lst[i - 1][1]
                h2 = lst[i][1]
                # calculate second point(lst[i][0], h) that starts at (lst[i-1][0],h1)
                h = h1 + abs(lst[i][0] - lst[i - 1][0])
                if h > h2:
                    h = h2 + (h - h2) // 2
                max_height = max(max_height, h)
                lst[i][1] = min(h, h2)
            return max_height

        # go from left to right
        calc_height(restrictions)
        # go from right to left
        return calc_height(restrictions[::-1])