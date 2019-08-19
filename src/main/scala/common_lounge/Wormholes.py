s=input()
n,x,y=s.split()
n=int(n)
x=int(x)
y=int(y)
contests = []
v = []
w = []
for i in range(n):
    s = input()
    arr = s.split()
    contests.append(map(lambda x:int(x), arr))

s = input()
v = [int(x) for x in s.split()]
s = input()
w = [int(x) for x in s.split()]

