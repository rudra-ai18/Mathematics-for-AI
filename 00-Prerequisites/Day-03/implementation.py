"""
Day 03 — Exponents & Logarithms
Run from the repository root in VS Code:
    python 00-Prerequisites/Day-03/implementation.py

Dependencies:
    python -m pip install numpy matplotlib
"""

import numpy as np
import matplotlib.pyplot as plt

# Logarithms require positive real inputs, so x starts above zero.
x = np.linspace(0.1, 5, 100)

# Exponential and polynomial functions.
y_exp2 = 2 ** x
y_expe = np.exp(x)
y_sq = x ** 2

# Logarithms with three common bases.
y_log2 = np.log2(x)
y_loge = np.log(x)       # natural log, ln(x)
y_log10 = np.log10(x)

# Plot 1: compare growth.
plt.figure(figsize=(10, 5))
plt.plot(x, y_exp2, label="2^x", linewidth=2)
plt.plot(x, y_expe, label="e^x", linewidth=2)
plt.plot(x, y_sq, label="x^2", linewidth=2)
plt.axhline(0, linewidth=0.5)
plt.axvline(0, linewidth=0.5)
plt.title("Exponential vs Polynomial Growth")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# Plot 2: compare logarithms.
plt.figure(figsize=(10, 5))
plt.plot(x, y_log2, label="log2(x)", linewidth=2)
plt.plot(x, y_loge, label="ln(x)", linewidth=2)
plt.plot(x, y_log10, label="log10(x)", linewidth=2)
plt.axhline(0, linewidth=0.5)
plt.axvline(0, linewidth=0.5)
plt.title("Logarithmic Functions")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# Quick calculations from the lesson.
print("2^10 =", 2**10)
print("log2(1024) =", np.log2(1024))
print("e^1 =", np.exp(1))
print("ln(e) =", np.log(np.exp(1)))

# Optional experiment: uncomment to observe invalid log input behavior.
# NumPy typically returns -inf and emits a RuntimeWarning for np.log(0).
# print("log(0) =", np.log(0))
