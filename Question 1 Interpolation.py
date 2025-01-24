def lagrange_interpolation(x_values, y_values, x):
    def L(k, x):
        result = 1
        for i in range(len(x_values)):
            if i != k:
                result *= (x - x_values[i]) / (x_values[k] - x_values[i])
        return result

    y = sum(y_values[k] * L(k, x) for k in range(len(x_values)))
    return y

x_values = [9, 3, 1]
y_values = [6, 5, 12]
x = 10
y_at_10 = lagrange_interpolation(x_values, y_values, x)
print("The value of y at x=10 is:", y_at_10)
