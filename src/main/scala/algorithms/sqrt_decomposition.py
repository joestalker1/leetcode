int sum = 0


def sqrt_decom(arr):
    n = len(arr)
    lenb = int(n ** 0.5) + 1
    b = []
    for i in range(n):
        b[i // lenb] += arr[i]
    l = 0
    r = 10
    c_l = l // lenb
    c_r = r // lenb
    sum = 0
    if c_l == c_r:
        for i in range(l,r+1):
            sum += arr[i]
        else:
            end = (c_l + 1) * lenb-1
            for i in range(l,end+1):
                sum += arr[i];
	    for i in range(c_l+1,c_r):
            sum += b[i]
	    for i in range(c_r*len,r+1):
            sum += arr[i]

   l = 1
   r = 10
    while True:
        sum = 0
        for i in range(l,r + 1):
            if i % lenb == 0 and i + lenb-1 <= r:
                sum += b[i // lenb]
                i += lenb
            else:
                sum += arr[i]
                i += 1
