
#Author: Dibash Bhusal322
# Define the function for f(x) = x^3 - 4x - 9
#BisectionMethod

import math
def d(x):
    return x**3 - 4*x - 9

# Initial interval
x1 = 2
x2 = 3

# Function values at initial points
y1 = d(x1)
y2 = d(x2)

# Check if root exists in the interval
if y1 * y2 > 0:
    print('No roots exist within the given interval')
    exit()

# Bisection method loop
for i in range(1, 101):
    # Midpoint of the interval
    xh = (x1 + x2) / 2
    yh = d(xh)
    
    # Check for convergence (close to zero with tolerance 0.001)
    if abs(yh) < 1.0e-3:
        break
    # Update the interval based on the sign of function values
    elif y1 * yh < 0:
        x2 = xh  # Update x2, x1 stays the same, no need to recalculate y1
    else:
        x1 = xh  # Update x1, so we need to recalculate y1
        y1 = yh  # Recalculate y1 only when x1 is updated

# Print the root and number of iterations
print('The root: %.3f' % xh)
print('Number of bisections: %d' % i)

