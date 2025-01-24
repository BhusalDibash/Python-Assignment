#Author: Dibash Bhusal322
#Question number 5
#Newton Raphson Method

import math

# Define the function d(x) = x^2 - 2x - 3
def d(x):
    return x**2 - 2*x - 3

# Define the derivative of the function d'(x) = 2x - 2
def d_prime(x):
    return 2*x - 2

# Define the Newton-Raphson method
def newton_raphson(x0, iterations):
    x = x0
    for i in range(iterations):
        x = x - d(x) / d_prime(x)
        print(f"Iteration {i+1}: x = {x:.6f}")
    return x

# Initial guess
x0 = 4
# Number of iterations
iterations = 4

# Call the Newton-Raphson method
root = newton_raphson(x0, iterations)

print(f"The root after {iterations} iterations is approximately: {root:.6f}")
