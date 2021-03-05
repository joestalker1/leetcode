# Use Heron's
def squareroot(n, error=0.00001):
    guess = 1
    while abs(guess ** 2 - n) >= error:
        guess = (guess + n / guess) / 2.0
    return guess


print(squareroot(10))
