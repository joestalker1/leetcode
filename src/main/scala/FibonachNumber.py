import math

def findFibPosition(n):
    pos = 2.078087 * math.log(n) + 1.672276
    return int(pos)

print(findFibPosition(3))