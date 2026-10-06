# Day 01 — Functions in Python
# Concepts: linear, quadratic, sine + manual function evaluation

import numpy as np
import matplotlib.pyplot as plt

# 100 points from -10 to 10
x = np.linspace(-10, 10, 100)

# Function 1: Linear
y1 = 2 * x + 3

# Function 2: Quadratic
y2 = x ** 2

# Function 3: Sine
y3 = np.sin(x)

# Plot the functions
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.plot(x, y1, linewidth=2)
plt.title("f(x) = 2x + 3")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True, alpha=0.3)

plt.subplot(1, 3, 2)
plt.plot(x, y2, linewidth=2)
plt.title("f(x) = x²")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True, alpha=0.3)

plt.subplot(1, 3, 3)
plt.plot(x, y3, linewidth=2)
plt.title("f(x) = sin(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Manual function
def f(x):
    return 2 * x + 3

print("f(0) =", f(0))
print("f(4) =", f(4))
print("f(-2) =", f(-2))

# Expected:
# f(0) = 3
# f(4) = 11
# f(-2) = -1
