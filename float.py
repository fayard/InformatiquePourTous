n = 100000
x = 0.0
for k in range(1, n + 1):
    x += 1.0 / k**2
y = 0.0
for k in range(n, 0, -1):
    y +=  1.0 / k**2
print repr(x), repr(y)

n = 6
def fact(n):
    result = 1
    for k in range (1, n + 1):
        result *= k
    return result
x = 0.0
for k in range(0, n + 1):
    x += 1.0 / fact(k)
y = 0.0
for k in range(n, -1, -1):
    y +=  1.0 / fact(k)
print repr(x), repr(y)

def var1(x):
    n = len(x)
    a = 0.0
    b = 0.0
    for k in range(n):
        a += x[k]
        b += x[k]**2
    return (b / n) - (a / n)**2

def var2(x):
    n = len(x)
    m = 0.0
    for k in range(n):
        m += x[k]
    m /= n
    v = 0.0
    for k in range(n):
        v += (x[k]-m)**2
    v /= n
    return v

n = 7
x = [ 1.0 - 10**(-n), 1.0, 1.0 + 10**(-n) ]
print var1(x), var2(x)


import math
def deriv(h):
    der = (math.sqrt(1.0 + h) - 1.0) / h
    print (der - 0.5)/0.5

deriv(10**(-3))
deriv(10**(-6))
deriv(10**(-8))
deriv(10**(-10))
deriv(10**(-13))

