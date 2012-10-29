import math
'''
For solving Bradie problem 6.2.4
'''
x0 = 2

def app(h):
    return (math.log(x0 + 2*h) - math.log(x0 - h))/(3*h)

A = []
for i in range(0, 10):
    A.append(10**(-i))

for i in A:
    print 'err = {} and h = {}'.format(abs((1./2) -  app(i)), i)
    print ''

