from math import log, factorial
import numpy as np

def div_dif(f1, f2, x1, x2):
    return (float(f2 - f1)/(x2 - x1))

# Calculate the linear interpolant at a point x. For Bradie 5.5.1
def inter(x, x0, x1, f0, f1):
    a0 = f0
    b0 = float(f1 - f0)/(x1 - x0)
    return a0 + b0*(x - x0)

def p(x):
    a = x - 1
    b = (2*log(2) - 1)*a*a
    c = x - 2
    e = (-3*log(2) + 2)*a*a*c
    h = .5*(1.5*log(3) + 2*log(2) - 3)*a*a*c*c
    f = x - 3
    g = .5*(1.5*log(3) + 2*log(2) - 3)*a*a*c*c*f
    return a + b + e + h + g

def er(x):
    a = .5
    b = .5
    c = 1.5
    return (24./(x**5))*(1./(factorial(6)))*a*a*b*b*c*c
#    return (x-1) + (2*log(2)-1)*(x-1)**2 + (-3*log(2)+2)*(x-1)**2 * (x-2) + (.75*log(3) +log(2) - .75)*(x-1)**2 * (x-2)**2 + (-2*log(3) + log(2) + 1.5)*(x-1)**2 * (x-2)**2 * (x-3)

def div_dif_table(xlist, flist, dflist):
    zlist = []
    for i in range(2*len(xlist)):
        zlist.append( xlist[i/2])
    fzlist = []
    for i in range(2*len(flist)):
        fzlist.append( flist[i/2])
    print zlist, fzlist
    # Initialize table.
    T = np.zeros((len(zlist)-1, len(zlist)-1))
    # Add derivative values to table.
    for i in range(len(dflist)):
        T[i*2, 0] = dflist[i]
    # Add div_dif values to first column.
    for i in range(1, len(T), 2):
        T[i, 0] = div_dif(fzlist[i], fzlist[i+1], zlist[i], zlist[i+1])
    # Populate the rest of the columns.
    for i in range(1, len(T)):
        for j in range(0, len(T) - i):
            f0 = T[j, i - 1]
            f1 = T[j + 1, i - 1]
            x0 = zlist[j]
            x1 = zlist[j + (1+ i)]
            print x0, x1
            T[j, i] = div_dif(f0, f1, x0, x1)
    return T


    
        
        


