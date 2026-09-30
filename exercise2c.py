# Exercise 2C - Influence of the Initial Approximation
#
# In this exercise I compare two different initial approximations
# for the Newton-Raphson method:
# p0 = 1.5 and p0 = 2.5
#
# I also compare the number of iterations required for
# different tolerances.


def f(x):
    # This is the function from Exercise 2
    return x**3 - 2*x - 2


def df(x):
    # This is the derivative of the function
    return 3*x**2 - 2


def newton_raphson(p0, tolerance):
    # I start with the initial approximation given
    p = p0

    # I start counting the iterations from zero
    iterations = 0

    while True:

        # I calculate the next approximation using Newton's formula
        p_new = p - f(p) / df(p)

        # I increase the iteration counter
        iterations += 1

        # I check if the difference between two consecutive
        # approximations is smaller than the required tolerance
        if abs(p_new - p) < tolerance:
            break

        # I update the approximation for the next iteration
        p = p_new

    return p_new, iterations


# I define the two initial approximations required in the exercise
initial_approximations = [1.5, 2.5]

# I define the tolerances required in the exercise
tolerances = [10**(-3), 10**(-5)]


# I store the results so that I can use them later
# in the discussion at the end of the program
results = {}


# I test both initial approximations
for p0 in initial_approximations:

    # I create a dictionary to store the results for each p0
    results[p0] = {}

    print("Initial approximation:", p0)

    # I test both tolerances
    for tolerance in tolerances:

        # I apply the Newton-Raphson method
        root, iterations = newton_raphson(p0, tolerance)

        # I save the result
        results[p0][tolerance] = (root, iterations)

        # I display the result in the terminal
        print("Tolerance:", tolerance)
        print("Approximate root:", root)
        print("Number of iterations:", iterations)
        print()

    print("----------------------------------------")
    print()

# Discussion / Conclusion
print("DISCUSSION / CONCLUSION")
print()

# I obtain the number of iterations for each case
iterations_15_3 = results[1.5][10**(-3)][1]
iterations_15_5 = results[1.5][10**(-5)][1]

iterations_25_3 = results[2.5][10**(-3)][1]
iterations_25_5 = results[2.5][10**(-5)][1]


print(
    "The Newton-Raphson method converges to the same root "
    "for both initial approximations."
)

print(
    "Using p0 = 1.5 requires "
    + str(iterations_15_3)
    + " iterations for a tolerance of 10^-3 and "
    + str(iterations_15_5)
    + " iterations for a tolerance of 10^-5."
)

print(
    "Using p0 = 2.5 requires "
    + str(iterations_25_3)
    + " iterations for a tolerance of 10^-3 and "
    + str(iterations_25_5)
    + " iterations for a tolerance of 10^-5."
)

print(
    "This shows that the initial approximation can influence "
    "the number of iterations required for convergence."
)

print(
    "In this particular problem, both initial approximations "
    "converge successfully to the same root, but the initial "
    "approximation p0 = 2.5 requires one additional iteration "
    "for the stricter tolerance of 10^-5."
)