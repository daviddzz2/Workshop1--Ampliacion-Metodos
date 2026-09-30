# Exercise 4 - Numerical Integration
#
# In this exercise I approximate the integral
#
#       I = integral from 0 to 2 of exp(-x^2) dx
#
# using:
# 1. The Composite Trapezoidal Rule
# 2. The Composite Simpson's 1/3 Rule
#
# I use n = 4 equal subintervals as requested in the exercise.
#
# At the end, I also compare the numerical results with a
# reference value of the integral and calculate the true errors.


import numpy as np
import matplotlib.pyplot as plt
import math


# ---------------------------------------------------------
# FUNCTION
# ---------------------------------------------------------

def f(x):
    # This is the function that we have to integrate
    return np.exp(-x**2)


# ---------------------------------------------------------
# INTERVAL AND NODES
# ---------------------------------------------------------

# I define the limits of integration
a = 0
b = 2

# The exercise asks us to use 4 equal subintervals
n = 4

# I calculate the width of each subinterval
h = (b - a) / n

# I create the integration nodes
x_nodes = np.linspace(a, b, n + 1)

# I calculate the function values at the integration nodes
y_nodes = f(x_nodes)


# ---------------------------------------------------------
# COMPOSITE TRAPEZOIDAL RULE
# ---------------------------------------------------------

# I calculate the Composite Trapezoidal approximation
trapezoidal_approx = h * (
    (y_nodes[0] + y_nodes[-1]) / 2
    + np.sum(y_nodes[1:-1])
)


# ---------------------------------------------------------
# TRAPEZOIDAL ERROR BOUND
# ---------------------------------------------------------

# For the Composite Trapezoidal Rule, the theoretical error is:
#
# |E_T| <= ((b-a)^3 / (12*n^2)) * max|f''(x)|
#
# For f(x) = exp(-x^2):
#
# f''(x) = (4*x^2 - 2)*exp(-x^2)
#
# The maximum absolute value on [0, 2] is 2.

max_f2 = 2

# I calculate the theoretical worst-case error bound
trapezoidal_error_bound = (
    ((b - a)**3) / (12 * n**2)
) * max_f2


# ---------------------------------------------------------
# COMPOSITE SIMPSON'S 1/3 RULE
# ---------------------------------------------------------

# Simpson's Rule requires an even number of subintervals.
# Since n = 4, it can be applied directly.

simpson_approx = (
    h / 3
    * (
        y_nodes[0]
        + y_nodes[-1]
        + 4 * (y_nodes[1] + y_nodes[3])
        + 2 * y_nodes[2]
    )
)


# ---------------------------------------------------------
# SIMPSON ERROR BOUND
# ---------------------------------------------------------

# For Simpson's Rule, the theoretical error is:
#
# |E_S| <= ((b-a)^5 / (180*n^4)) * max|f^(4)(x)|
#
# For f(x) = exp(-x^2):
#
# f^(4)(x) = (16*x^4 - 48*x^2 + 12)*exp(-x^2)
#
# The maximum absolute value on [0, 2] is 12.

max_f4 = 12

# I calculate the theoretical worst-case error bound
simpson_error_bound = (
    ((b - a)**5) / (180 * n**4)
) * max_f4


# ---------------------------------------------------------
# REFERENCE INTEGRAL
# ---------------------------------------------------------

# The integral of exp(-x^2) does not have an elementary
# antiderivative, so I use the numerical reference value
# obtained from the error function.
#
# integral from 0 to 2 of exp(-x^2) dx
# = sqrt(pi)/2 * erf(2)

reference_integral = (
    math.sqrt(math.pi) / 2 * math.erf(2)
)


# ---------------------------------------------------------
# TRUE ABSOLUTE ERRORS
# ---------------------------------------------------------

# I calculate the absolute difference between each
# numerical approximation and the reference value.

trapezoidal_absolute_true_error = abs(
    reference_integral - trapezoidal_approx
)

simpson_absolute_true_error = abs(
    reference_integral - simpson_approx
)


# ---------------------------------------------------------
# PRINT RESULTS
# ---------------------------------------------------------

print()
print("==============================================")
print("NUMERICAL INTEGRATION RESULTS")
print("==============================================")

print()
print("Number of subintervals:", n)
print("Step size:", h)

print()
print("Trapezoidal approximation:")
print(trapezoidal_approx)

print()
print("Trapezoidal error bound:")
print(trapezoidal_error_bound)

print()
print("Simpson approximation:")
print(simpson_approx)

print()
print("Simpson error bound:")
print(simpson_error_bound)

print()
print("Reference integral:")
print(reference_integral)

print()
print("Trapezoidal absolute true error:")
print(trapezoidal_absolute_true_error)

print()
print("Simpson absolute true error:")
print(simpson_absolute_true_error)

print()
print("==============================================")


# ---------------------------------------------------------
# GRAPHICAL REPRESENTATION
# ---------------------------------------------------------

# I create many points so that the original function
# appears smooth in the graphs.
x = np.linspace(a, b, 500)
y = f(x)


# I create ONE figure containing both graphs.
# This means that both numerical methods will be displayed
# in the same window.
fig, axes = plt.subplots(1, 2, figsize=(14, 6))


# =========================================================
# LEFT GRAPH - TRAPEZOIDAL RULE
# =========================================================

# I select the first graph
ax1 = axes[0]

# I plot the original function
ax1.plot(
    x,
    y,
    label="f(x) = exp(-x^2)"
)

# I plot the integration nodes
ax1.scatter(
    x_nodes,
    y_nodes,
    label="Integration nodes",
    zorder=3
)


# I draw each trapezoid
for i in range(n):

    # I obtain the two nodes of the current interval
    x1 = x_nodes[i]
    x2 = x_nodes[i + 1]

    # I obtain the corresponding function values
    y1 = y_nodes[i]
    y2 = y_nodes[i + 1]

    # I fill the area corresponding to the trapezoid
    ax1.fill(
        [x1, x1, x2, x2],
        [0, y1, y2, 0],
        alpha=0.3
    )

    # I draw the straight line used by the
    # Trapezoidal Rule
    ax1.plot(
        [x1, x2],
        [y1, y2],
        linestyle="--"
    )


# I add labels and a title
ax1.set_title("Composite Trapezoidal Rule")
ax1.set_xlabel("x")
ax1.set_ylabel("f(x)")

# I show the integration nodes on the x-axis
ax1.set_xticks(x_nodes)

# I add a grid and legend
ax1.grid()
ax1.legend()


# =========================================================
# RIGHT GRAPH - SIMPSON'S 1/3 RULE
# =========================================================

# I select the second graph
ax2 = axes[1]

# I plot the original function
ax2.plot(
    x,
    y,
    label="f(x) = exp(-x^2)"
)

# I plot the integration nodes
ax2.scatter(
    x_nodes,
    y_nodes,
    label="Integration nodes",
    zorder=3
)


# Simpson's Rule uses two subintervals at a time.
# With n = 4, there are two parabolic approximations:
# [0, 1] and [1, 2].

for i in range(0, n, 2):

    # I take three consecutive Simpson nodes
    x0 = x_nodes[i]
    x1 = x_nodes[i + 1]
    x2 = x_nodes[i + 2]

    y0 = y_nodes[i]
    y1 = y_nodes[i + 1]
    y2 = y_nodes[i + 2]

    # I calculate the quadratic polynomial passing
    # through the three Simpson nodes.
    coefficients = np.polyfit(
        [x0, x1, x2],
        [y0, y1, y2],
        2
    )

    # I create many points between x0 and x2
    # to draw the parabola smoothly.
    x_parabola = np.linspace(x0, x2, 100)

    # I calculate the value of the parabola
    # at those points.
    y_parabola = np.polyval(
        coefficients,
        x_parabola
    )

    # I draw the parabolic approximation
    ax2.plot(
        x_parabola,
        y_parabola,
        linestyle="--",
        label="Simpson parabola" if i == 0 else None
    )

    # I fill the area below the parabola
    ax2.fill_between(
        x_parabola,
        y_parabola,
        0,
        alpha=0.3
    )


# I add labels and a title
ax2.set_title("Composite Simpson's 1/3 Rule")
ax2.set_xlabel("x")
ax2.set_ylabel("f(x)")

# I show the integration nodes on the x-axis
ax2.set_xticks(x_nodes)

# I add a grid and legend
ax2.grid()
ax2.legend()


# ---------------------------------------------------------
# FINAL GRAPH
# ---------------------------------------------------------

# I adjust the spacing between both graphs
plt.tight_layout()

# I display both graphs in the same window
plt.show()