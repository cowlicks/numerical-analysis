'''
    2. Implement the Newton method in matlab. Use it to find the root of
            f(x) = ln(1 + x) - cosx
        in (0,1). Start with p0 = 0. For the stopping critera, stop at
        iteration n if
            |pn - pn-1| <= e
        with e = 1e-6. Print the values for i = 1,...,n.
'''
import math

# Define our function and it's derivative.
def f(x):
    return math.log(1 + x) - math.cos(x)

def df(x):
    return math.sin(x) + 1./(1 + x)

# The Newton's method iteration function.
def n(x):
    return x - f(x)/df(x)

# Stopping criteria.
e = 1e-6

# Initial guess.
p0 = 0

# Iteration counter.
count = 1

# Algorithim.
while True:
    p1 = n(p0)
    print "p{} = {}".format(count, p1)

    # Check stopping critria.
    if abs(p1 - p0) <= 1e-6:
        break
    else:
        p0 = p1
    count +=1
