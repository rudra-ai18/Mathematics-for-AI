# Day 02 Notes — Functions in AI/ML

## 1. Intuition

On Day 1, we learned that a function maps an input to an output: y = f(x).

In machine learning, we usually do not know the exact function in advance. We use examples in data to learn a function that maps inputs to useful predictions.

## 2. House-price example

The study material gives these examples:

| Size (sq ft), x | Actual price |
|---:|---:|
| 1000 | ₹50,00,000 |
| 1500 | ₹75,00,000 |
| 2000 | ₹1,00,00,000 |
| 2500 | ₹1,25,00,000 |

We want a function: Price = f(Size).

A possible linear model is f(x) = mx + b. Here, m and b are parameters learned from data.

## 3. Parameters

| Symbol | Meaning |
|---|---|
| x | Input feature (house size) |
| y | Output/prediction |
| m | Slope: how quickly the prediction changes as size changes |
| b | Intercept: model prediction when size is zero |
| m, b | Parameters the model learns |

The goal is to choose values of m and b that make predictions fit the data well.

## 4. Prediction and error

For the given example, the study material tries m = 0.05 lakhs per square foot and b = 0 when price is measured in lakhs.

prediction = m × size + b

error = actual price − prediction

When a line matches every point in this example, the errors are zero. Real-world data is often noisy, so points may not all lie on one straight line; then we seek a line that fits well.

## 5. Visual intuition

- Scatter points represent observed data.
- The line represents the model's predictions.
- The distance between an observed point and the prediction reflects the error for that point.
- Changing m changes the line's slope.
- Changing b shifts the line up or down.

## 6. AI/ML connection

| In the exercise | In machine learning |
|---|---|
| m * size + b | Linear regression model |
| Trying values of m and b | Choosing model parameters |
| Comparing predictions with actual values | Measuring prediction error |
| Finding a good-fitting line | Model fitting/optimization |

Neural networks use more complex parameterized functions, but the broad idea is similar: learn parameters from data so predictions become useful.

**Important:** This lesson introduces the idea of error and fitting. Loss functions and optimization methods such as gradient descent are studied later.
