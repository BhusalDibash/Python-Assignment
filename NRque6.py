#Author: Dibash Bhusal322
#Question number 6
#Newton Raphson Method

import math

# Initial guess
x0 = 0.5
# Number of iterations
iterations = 5
def d(x):
    return x**3 - x + 1

def d_prime(x):
    return 3*x**2 - 1

def newton_raphson(x0, iterations):
    x = x0
    for i in range(iterations):
        x = x - d(x) / d_prime(x)
        print(f"Iteration {i+1}: x = {x}")
    return x

root = newton_raphson(x0, iterations)
print(f"Root after {iterations} iterations: {root}")
