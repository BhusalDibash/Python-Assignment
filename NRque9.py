#Author: Dibash Bhusal322
#Question number 9
#Newton Raphson Method

import math  

# Define the function f(x) = x^3 - 6x^2 + 11x
def d(x):
    return x**3 - 6*x**2 + 11*x
# Initial guess
x0 = 3.0

# Define the derivative of the function f'(x) = 3x^2 - 12x + 11
def d_prime(x):
    return 3*x**2 - 12*x + 11

# Implement the Newton-Raphson method
def newton_raphson(x0, tolerance=1e-6, max_iterations=100):
    x = x0  

