mkrec = lambda f: f(f)

fact = mkrec(lambda rec: lambda x:
  1 if x == 0 else rec(rec)(x - 1) * x)

print(fact(3))

f1 = (1,3)
f2 = (2,5)


def gcd(a, b):
  if b == 0:
    return a
  return gcd(b, a % b)


def lcm(f1, f2):
  (a,b) = f1
  (d,c) = f2
  gcd_ = gcd(max(b,c), min(b,c))
  return (b * c) // gcd_


print(lcm(f1,f2))
