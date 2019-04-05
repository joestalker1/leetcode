# a and b are index in an array
# x and y are indiced in a segment tree

def sum(tree, a, b, k, x, y):
    if b < x or a > y:
        return 0
    if a <= x and y <= b:
        return tree[k]
    d = (x + y) // 2
    return sum(tree, a, b, 2 * k, x, d) + sum(tree, a, b, 2 * k + 1, d + 1, y)

class DynTree:
    def __init__(self, a, x, y):
        self.value = a
        self.x = x
        self.y = y
        self.left = None
        self.right = None
        