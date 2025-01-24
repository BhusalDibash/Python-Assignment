#Author: Dibash Bhusal322
#Question number 9
#Newton Raphson Method

import math

# Define the function f(x) = x * sin(x) - 1
def f(x):
    return x * math.sin(x) - 1
# Initial guess
x0 = 1.0

# Define the derivative of the function f'(x) = sin(x) + x * cos(x)
def f_prime(x):
    return math.sin(x) + x * math.cos(x)

# Implement the Newton-Raphson method
def newton_raphson(x0, tolerance=1e-6, max_iterations=100):
    x = x0  # Initialize x with the initial guess x0
    for i in range(max_iterations):  # Iterate up to max_iterations times
        x_new = x - f(x) / f_prime(x)  # Apply the Newton-Raphson formula
        if abs(x_new - x) < tolerance:  # Check if the result is within the desired tolerance
            return x_new  # Return the root if within tolerance
        x = x_new  # Update x to the new value
    return x  # Return the root if max_iterations is reached

# Find the root using the Newton-Raphson method
root = newton_raphson(x0)
print(f"Root: {root:.6f}")  # Print the root rounded to 6 decimal places
