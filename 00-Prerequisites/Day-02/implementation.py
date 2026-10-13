"""
Day 02 — Functions in AI/ML
Explore a parameterized linear model: prediction = m * size + b.

Run locally in VS Code:
    python 00-Prerequisites/Day-02/implementation.py

Dependencies:
    python -m pip install numpy matplotlib
"""

import numpy as np
import matplotlib.pyplot as plt

# Example data from the lesson: house size (sq ft) and price (₹ lakhs).
size = np.array([1000, 1500, 2000, 2500, 3000], dtype=float)
actual_price = np.array([50, 75, 100, 125, 150], dtype=float)

# Change these parameters to see how the model line moves.
m = 0.05  # slope: lakhs per square foot
b = 0.0   # intercept: predicted lakhs at size zero

# Parameterized function: f(x) = m*x + b
predicted_price = m * size + b
errors = actual_price - predicted_price

print("Actual prices (₹ lakhs):", actual_price)
print("Predicted prices (₹ lakhs):", predicted_price)
print("Errors (actual - predicted):", errors)

# Plot observations and the model's predictions.
plt.figure(figsize=(9, 6))
plt.scatter(
    size,
    actual_price,
    color="red",
    s=85,
    label="Observed data",
    zorder=3,
)

# Use a smooth range for the candidate line.
size_line = np.linspace(size.min(), size.max(), 200)
price_line = m * size_line + b
plt.plot(
    size_line,
    price_line,
    color="blue",
    linewidth=2,
    label=f"Model: f(x) = {m}x + {b}",
)

plt.xlabel("House size (sq ft)")
plt.ylabel("Price (₹ lakhs)")
plt.title("Learning a Function from Data — Day 2")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# Try different values of m and b, then rerun this file.
