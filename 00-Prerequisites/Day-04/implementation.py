"""
Day 04 — Coordinate Geometry
Run from the repository root in VS Code:
    python 00-Prerequisites/Day-04/implementation.py

Dependency:
    python -m pip install matplotlib
"""

import math
import matplotlib.pyplot as plt

# Change these points for the practice task.
A = (1, 2)
B = (4, 6)

delta_x = B[0] - A[0]
delta_y = B[1] - A[1]

distance = math.sqrt(delta_x**2 + delta_y**2)
midpoint = ((A[0] + B[0]) / 2, (A[1] + B[1]) / 2)

# Slope is undefined for a vertical line.
slope = None if delta_x == 0 else delta_y / delta_x

print(f"Point A: {A}")
print(f"Point B: {B}")
print(f"Distance: {distance}")
print(f"Midpoint: {midpoint}")
print("Slope: undefined (vertical line)" if slope is None else f"Slope: {slope}")

# Plot points and the connecting segment.
plt.figure(figsize=(8, 8))
plt.scatter([A[0], B[0]], [A[1], B[1]], s=120, label="Points A and B", zorder=5)
plt.plot([A[0], B[0]], [A[1], B[1]], linestyle="--", linewidth=2, label="Segment AB")

plt.text(A[0] - 0.35, A[1] + 0.25, f"A{A}")
plt.text(B[0] + 0.1, B[1] + 0.25, f"B{B}")
plt.scatter([midpoint[0]], [midpoint[1]], marker="x", s=100, label=f"Midpoint {midpoint}")

# Draw the right triangle that illustrates delta x and delta y.
plt.plot([A[0], B[0]], [A[1], A[1]], linestyle=":", label="Horizontal difference")
plt.plot([B[0], B[0]], [A[1], B[1]], linestyle=":", label="Vertical difference")

plt.axhline(0, linewidth=0.6)
plt.axvline(0, linewidth=0.6)
plt.grid(True, alpha=0.3)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Coordinate Geometry: Points, Distance, and Midpoint")
plt.gca().set_aspect("equal", adjustable="box")
plt.legend()
plt.tight_layout()
plt.show()

# Extra experiment: compare four points and calculate pairwise distances.
points = [(1, 1), (2, 3), (3, 2), (5, 5)]
print("\nPairwise distances:")
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        p, q = points[i], points[j]
        d = math.dist(p, q)
        print(f"{p} to {q}: {d:.3f}")
