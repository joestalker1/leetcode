from collections import deque


class Solution:
    def floodFill(self, image, sr: int, sc: int, newColor: int):
        if not image:
            return image
        q = deque()
        q.append([sr,sc])
        prev_clr = image[sr][sc]
        while q:
            r, c = q.popleft()
            image[r][c] = -newColor
            for r1, c1 in [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]:
                if 0 <= r1 < len(image) and 0 <= c1 < len(image[0]) and image[r1][c1] == prev_clr:
                    q.append([r1, c1])
        for r in range(len(image)):
            for c in range(len(image[0])):
                image[r][c] = abs(image[r][c])
        return image
