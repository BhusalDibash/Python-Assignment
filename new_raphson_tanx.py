
import math


x = 1.0 

# Newton-Raphson iteration
for iteration in range(1,101 ):
    xnew = x - (math.tan(x) - x) / (1 / math.cos(x)**2 - 1)
    if abs(xnew - x) < 0.0001: 
        break
    x = xnew

print('The root : %0.5f' % xnew)
print('The number of iterations : %d' % iteration)
