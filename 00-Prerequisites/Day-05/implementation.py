"""
Day 05 — Scalars & Vectors
Run from the repository root in VS Code:
    python 00-Prerequisites/Day-05/implementation.py

Dependencies:
    python -m pip install numpy matplotlib
"""

import numpy as np
import matplotlib.pyplot as plt

# Define vectors.
v = np.array([3, 4], dtype=float)
u = np.array([1, 2], dtype=float)

# Magnitude, vector addition, and scalar multiplication.
magnitude_v = np.linalg.norm(v)
w = v + u
scaled = 2 * v

print(f"v = {v}")
print(f"Magnitude of v = {magnitude_v}")
print(f"u = {u}")
print(f"v + u = {w}")
print(f"2 * v = {scaled}")

def draw_vector(ax, vector, label):
    """Draw a vector as an arrow from the origin."""
    ax.quiver(
        0, 0, vector[0], vector[1],
        angles="xy", scale_units="xy", scale=1,
        label=f"{label} = ({vector[0]:g}, {vector[1]:g})"
    )

fig, ax = plt.subplots(figsize=(8, 8))
draw_vector(ax, v, "v")
draw_vector(ax, u, "u")
draw_vector(ax, w, "v + u")
draw_vector(ax, scaled, "2v")

ax.axhline(0, linewidth=0.6)
ax.axvline(0, linewidth=0.6)
ax.grid(True, alpha=0.3)
ax.set_xlim(-1, 8)
ax.set_ylim(-1, 10)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Vectors: Addition and Scalar Multiplication")
ax.set_aspect("equal", adjustable="box")
ax.legend()
fig.tight_layout()
plt.show()

# Experiment: magnitude and scaling.
test_vector = np.array([5, 12], dtype=float)
print(f"\nVector {test_vector} has magnitude {np.linalg.norm(test_vector)}")

c = np.array([3, 4], dtype=float)
fig, ax = plt.subplots(figsize=(7, 7))
for factor in (0.5, 1, 2):
    draw_vector(ax, factor * c, f"{factor:g}c")
ax.axhline(0, linewidth=0.6)
ax.axvline(0, linewidth=0.6)
ax.grid(True, alpha=0.3)
ax.set_xlim(-1, 8)
ax.set_ylim(-1, 10)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Scalar Multiplication: c, 0.5c, and 2c")
ax.set_aspect("equal", adjustable="box")
ax.legend()
fig.tight_layout()
plt.show()
