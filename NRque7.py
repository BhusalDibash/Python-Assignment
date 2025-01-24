#Author: Dibash Bhusal322
#Question number 7
#Newton Raphson Method


import math
#Determine the root of f(x)=tan(x)-x

x = 4.5

# Newton-Raphson iteration
for iteration in range(1,101 ):
    xnew = x - (math.tan(x) - x) / (1 / math.cos(x)**2 - 1)
    if abs(xnew - x) < 0.0001: 
        break
    x = xnew

print('The root : %0.5f' % xnew)
print('The number of iterations : %d' % iteration)

