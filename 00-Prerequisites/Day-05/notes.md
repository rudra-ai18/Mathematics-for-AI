# Day 05 Notes — Scalars & Vectors

## 1. Intuition

A scalar is a single number. A vector is an ordered list of numbers that can describe several features together.

For example, a house cannot be described fully by only its size or price. A feature vector could contain size, bedrooms, price, and a location score.

## 2. Real-life examples from the lesson

- **Weather:** temperature = 35°C is a scalar; a weather report can collect several measurements.
- **GPS directions:** moving 3 metres east and 4 metres north can be represented by the vector (3, 4).
- **Student report card:** (85, 90, 78, 82) is a 4-dimensional vector of scores.
- **RGB color:** red = (255, 0, 0), green = (0, 255, 0), blue = (0, 0, 255), white = (255, 255, 255).

## 3. Mathematical definitions

**Scalar:** a single real number, such as 5, -3.2, 0, 100, or π.

**Vector:** an ordered list of numbers, such as v = (3, 4) or v = [3, 4].

A 3D vector can be written v = (v₁, v₂, v₃). Its components correspond to coordinates/dimensions; n can denote the number of dimensions.

## 4. Magnitude (length)

For a 2D vector v = (x, y):

||v|| = √(x² + y²)

Example: v = (3, 4)

||v|| = √(3² + 4²) = √25 = 5

Another example: v = (6, 8) has magnitude 10.

## 5. Vector addition

Add corresponding components.

If u = (1, 2) and v = (3, 4):

u + v = (1 + 3, 2 + 4) = (4, 6)

Vector subtraction works the same way: subtract corresponding components.

## 6. Scalar multiplication

Multiply every component by the scalar.

If v = (3, 4) and c = 2:

cv = (2 × 3, 2 × 4) = (6, 8)

Multiplying by a positive scalar changes the magnitude by that factor and keeps the direction the same. Multiplying by a negative scalar reverses direction; multiplying by zero produces the zero vector.

## 7. Visual intuition

A vector can be drawn as an arrow from the origin to its coordinate endpoint.

- The arrow's direction represents direction.
- The arrow's length represents magnitude.
- The arrow for u + v is the resultant vector.
- The vector 2v points in the same direction as v and is twice as long when the scalar is positive.

## 8. AI/ML connection

**Feature vectors:** a data row can be represented as a vector of features, such as (age, blood pressure, heart rate, cholesterol).

**Word embeddings:** words can be represented as vectors; vector relationships help models represent aspects of language.

**Neural-network weights:** model parameters include arrays and vectors that are updated during training.

**Image pixels:** a 28 × 28 grayscale image contains 784 pixel values and can be flattened into a 784-dimensional vector.

Source: Day 5 — Scalars & Vectors study PDF.
