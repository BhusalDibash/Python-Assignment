#Author:Rajan_635
import math

# Define the function f(x) = cos(x) - x
def f(x):
    return math.cos(x) - x

# Initial interval [a, b]
a = 0
b = 1

# Function values at the endpoints
fa = f(a)
fb = f(b)

# Check if the root exists in the interval
if fa * fb > 0:
    print('No root exists within the given interval')
    exit()

# Tolerance and maximum number of iterations
tolerance = 1.0e-6
max_iterations = 100

# Bisection method loop
for i in range(1, max_iterations + 1):
    # Midpoint
    c = (a + b) / 2
    fc = f(c)
    
    # Check if the root is found or if the interval is sufficiently small
    if abs(fc) < tolerance or abs(b - a) < tolerance:
        break
    
    # Update the interval based on the sign of f(c)
    if fa * fc < 0:
        b = c  # The root is in the left half [a, c]
    else:
        a = c  # The root is in the right half [c, b]
        fa = fc  # Update fa since we moved a

# Print the root and the number of iterations
print('The root: %.1f' % c)
print('Number of iterations: %d' % i)
