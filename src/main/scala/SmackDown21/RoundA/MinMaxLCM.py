# cook your dish here
def input_data():
    t = int(input().strip())
    for _ in range(t):
        arr = input().strip().split(' ')
        x = int(arr[0])
        k = int(arr[1])
        max_lcm = (x*k - 1)*x*k
        min_lcm = x*2
        print('{} {}'.format(min_lcm,max_lcm))
input_data()