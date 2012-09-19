'''
    1. Implement the bisection method in matlab. Use it to find the root of
            f(x) = ln(1 + x) - cos(x)
        in (0, 1). Start with a1 = 0 and b1 = 1. For the stopping criteria, use
            |bn - an|/2 <= e
        with e = 1e-6 . Print the values of pi for i = 1,...,n.
'''
import math

# Define our function.
def f(x):
    return math.log(1 + x) - math.cos(x)

# Initial values & stopping criteria.
a, b, e = 0., 1., 1e-6

# Iteration counter.
count = 0

# Algorithim
while abs(a - b)/2. > e:
    # Get p and print it.
    p = (a + b)/2.
    print "p{} = {}".format(count, p)
    
    # Check for soln.
    if f(p) == 0:
        print "The root is x = {}".format(p)

    elif f(p) * f(a) < 0.:
        b = p

    elif f(p) * f(b) < 0.:
        a = p

    # Increment counter.
    count += 1

