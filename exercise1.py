# Exercise 1B - Bisection Method
# I use the Bisection Method to approximate the root of:
# f(x) = x^3 + x - 3

def f(x):
    # This is the function from the exercise
    return x**3 + x - 3


def bisection(a, b, tolerance):
    # I start the iteration counter at zero
    iterations = 0

    # I continue while the error estimate is bigger than the tolerance
    while (b - a) / 2 > tolerance:

        # I calculate the midpoint of the current interval
        p = (a + b) / 2

        # I increase the number of iterations
        iterations += 1

        # I check which half of the interval contains the root
        if f(a) * f(p) < 0:
            # The root is between a and p
            b = p
        else:
            # The root is between p and b
            a = p

    # I use the midpoint of the final interval as the root approximation
    p = (a + b) / 2

    return p, iterations


# I use the initial interval given in the exercise
a = 1
b = 1.5

# I test the two required tolerances
tolerances = [10**(-3), 10**(-5)]

for tolerance in tolerances:

    # I apply the Bisection Method
    root, iterations = bisection(a, b, tolerance)

    # I display the results
    print("Tolerance:", tolerance)
    print("Approximate root:", root)
    print("Number of iterations:", iterations)
    print()