#Author: Dibash Bhusal322
#Question number 8
#Newton Raphson Method
import math
# Define the function f(x) = ln(x) - 1
def d(x):
    return math.log(x) - 1
# Initial guess
x0 = 2.0

# derivative nikaleko d'(x) = 1/x
def d_prime(x):
    return 1 / x

# Implementing the Newton-Raphson method
def newton_raphson(x0, tolerance=1e-3, max_iterations=100):
    x = x0  
    for i in range(max_iterations):  
        x_new = x - d(x) /d_prime(x)  # Newton-Raphson formula
        if abs(x_new - x) < tolerance:  # Check if the result is within the desired tolerance
            return round(x_new, 3)  # Return the root rounded to 3 decimal places
        x = x_new  # naya value ma x lai update gareko
    return round(x, 3)  # Return the root if max_iterations is reached


#  Newton-Raphson method use garera root nikaleko
root = newton_raphson(x0)
print(f"Root: {root}")  # Print the root