n1,n2,n3 = map(int, input().split())
list1 = []
list2 = []
list3 = []
for i in range(n1):
    c = int(input())
    list1.append(c)

for i in range(n2):
    c = int(input())
    list2.append(c)

for i in range(n3):
    c = int(input())
    list3.append(c)

def merge(l1, l2, l3):
    i1 = 0
    i2 = 0
    i3 = 0
    res = []
    while i1 < len(l1) or i2 < len(l2) or i3 < len(l3):
        matched = False
        if i1 < len(l1):
            a = l1[i1]
            if i2 < len(l2) and l2[i2] == a:
                i2 += 1
                matched = True
            if i3 < len(l3) and l3[i3] == a:
                i3 += 1
                matched = True
            if matched:
                res.append(a)
                i1 += 1

        if not matched and i2 < len(l2):
            a = l2[i2]
            if i3 < len(l3) and l3[i3] == a:
                matched = True
                i3 += 1
            if matched:
                res.append(a)
                i2 += 1

        if not matched:
            i1 += 1
            i2 += 1
            i3 += 1
    return res
#],[21],[21,22])
#res = merge([23,  30,  42,57],[21,  23,  35,  57,    92],[21,  23,  30,  57,  90])
res = merge(list1 ,list2, list3)

print(len(res))
for x in res:
    print(x)
