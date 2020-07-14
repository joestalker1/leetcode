def countStringABC(n, bc, cc):
    print('{} b{} c{}'.format(n, bc, cc))
    if n == 0:
        return 1
    if bc < 0 or cc < 0:
        return 0
    if bc == 0 and cc == 0:
        return 1
    count = countStringABC(n-1,bc, cc)
    count += countStringABC(n-1, bc-1, cc)
    count += countStringABC(n-1, bc, cc-1)
    return count

print(countStringABC(3, 1, 2))

