# Exercise 2B - Newton-Raphson Method
# I use the Newton-Raphson Method to find the root of:
# f(x) = x^3 - 2x - 2

def f(x):
    # This is the original function
    return x**3 - 2*x - 2


def df(x):
    # This is the derivative of the function
    return 3*x**2 - 2


def newton_raphson(p0, tolerance):
    # I start the iteration counter at zero
    iterations = 0

    # I use the initial approximation given to the method
    p = p0

    while True:

        # I calculate the next Newton-Raphson approximation
        p_new = p - f(p) / df(p)

        # I count this iteration
        iterations += 1

        # I check if the difference between two consecutive
        # approximations is smaller than the required tolerance
        if abs(p_new - p) < tolerance:
            break

        # I update the approximation for the next iteration
        p = p_new

    return p_new, iterations


# I use the initial approximation from the exercise
p0 = 1.5

# I test both required tolerances
tolerances = [10**(-3), 10**(-5)]

for tolerance in tolerances:

    # I apply Newton-Raphson
    root, iterations = newton_raphson(p0, tolerance)

    # I display the results
    print("Tolerance:", tolerance)
    print("Approximate root:", root)
    print("Number of iterations:", iterations)
    print()