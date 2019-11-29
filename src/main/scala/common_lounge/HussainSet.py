s = input(' ')
arr = s.split()
n = int(arr[0])
m = int(arr[1])
# nums

nums1 = []
s = input(' ')
words = s.split()
for a in words:
    nums1.append(int(a))

nums1.sort(reverse=True)
nums2 = []

def get_max():
    if not nums2:
        return int(nums1.pop(0))
    if not nums1:
        return nums2.pop(0)
    a = int(nums1[0])
    if a > nums2[0]:
        nums1.pop(0)
        return a
    return nums2.pop(0)


i = 1
while m > 0:
    t = int(input())
    a = None
    while i <= t:
        a = get_max()
        b = a >> 1
        nums2.append(b)
        i += 1
    print(a)
    m -= 1




