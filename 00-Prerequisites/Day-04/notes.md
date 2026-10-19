# Day 04 Notes — Coordinate Geometry

## 1. Intuition

A coordinate system is a map for locating points.

- Moving right increases x.
- Moving up increases y.
- A point is written as (x, y).
- The origin is (0, 0).

In machine learning, a data point can represent features such as house size and price, or math and science scores. Data with many features can be represented in higher-dimensional spaces.

## 2. Real-life examples

- GPS: latitude and longitude locate a position on Earth.
- Chessboard: a square has a unique coordinate-like label.
- Movie ratings: action and comedy scores can form a point such as (2, 9).

## 3. Distance between two points

For A = (x₁, y₁) and B = (x₂, y₂):

d = √((x₂ − x₁)² + (y₂ − y₁)²)

This follows from the Pythagorean theorem: the horizontal and vertical differences form the two shorter sides of a right triangle.

### Worked example

A = (1, 2), B = (4, 6)

d = √((4 − 1)² + (6 − 2)²)  
d = √(3² + 4²) = √25 = 5

## 4. Midpoint

For A = (x₁, y₁) and B = (x₂, y₂):

M = ((x₁ + x₂)/2, (y₁ + y₂)/2)

Example: the midpoint of (2, 4) and (6, 8) is (4, 6).

## 5. Slope of a line

For two points with different x-coordinates:

m = (y₂ − y₁)/(x₂ − x₁)

- Positive slope: the line rises as x increases.
- Negative slope: the line falls as x increases.
- Zero slope: horizontal line.
- Vertical line: the slope is undefined because x₂ − x₁ = 0.

Example: between (1, 3) and (4, 9), m = (9 − 3)/(4 − 1) = 2.

## 6. Equation of a line

y = mx + b

- m is the slope.
- b is the y-intercept, where the line crosses the y-axis.

This is the same equation introduced on Day 2. Coordinate geometry gives it a visual meaning.

## 7. AI/ML connection

**Feature space:** each observation becomes a point whose coordinates are feature values. Two features make a 2D point; more features produce higher-dimensional representations.

**Distance metrics and KNN:** distances can help identify nearby examples. KNN, clustering, and recommendation systems can use notions of similarity based on distance.

**Decision boundaries:** classifiers may separate classes using lines or more complex boundaries in feature space.

**Scatter plots:** visualizing points can reveal patterns, clusters, and outliers.

**Caution:** features measured on very different scales can dominate Euclidean distance. Feature scaling may be needed in practical ML workflows; this is an additional practical note.

## 8. Python visualization

The implementation plots points A and B, the connecting line, a right triangle illustrating the coordinate differences, and the midpoint. It prints distance, midpoint, and slope.

Source: Day 4 — Coordinate Geometry study PDF.
