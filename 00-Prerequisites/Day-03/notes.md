# Day 03 Notes — Exponents & Logarithms

## 1. Intuition

**Exponent:** describes repeated multiplication. If a quantity doubles every hour, its count grows exponentially: 1, 2, 4, 8, 16, 32, ...

**Logarithm:** asks how many times a base must be multiplied by itself to produce a value. For example, log base 2 of 32 is 5 because 2^5 = 32.

## 2. Examples from the lesson

- Paper folding: each fold doubles the thickness.
- Compound interest: growth compounds over time.
- Earthquake scale: the lesson uses the Richter scale to illustrate logarithmic comparison.

Exponential growth can start slowly and then increase rapidly. A logarithm grows more slowly and can make a wide range of values easier to compare.

## 3. Mathematics

Exponent:

a^n = a × a × ... × a (n factors)

- a is the base.
- n is the exponent/power.
- a^n is the result.

The special constant e is approximately 2.718. The natural logarithm uses base e and is written ln(x).

Logarithm:

log_b(x) = n means b^n = x.

Common bases in this lesson:

| Base | Name | Example use |
|---|---|---|
| 10 | Common logarithm | General calculations |
| 2 | Binary logarithm | Computer science and information theory |
| e | Natural logarithm, ln | Calculus and machine learning |

## 4. Important rules

- Same base multiplication: a^m × a^n = a^(m+n)
- Product rule: log(ab) = log(a) + log(b)
- Power rule: log(a^n) = n log(a)

These logarithm rules assume valid positive inputs and a valid logarithm base.

## 5. Worked example

log base 2 of 64 = 6, because 2^6 = 64.

## 6. Visual intuition

The PDF compares:
- y = x: linear growth, a straight line.
- y = x^2: polynomial growth.
- y = 2^x: exponential growth.
- y = log(x): logarithmic growth.

The exponential and logarithmic functions with the same base are inverse functions over their valid domains.

## 7. AI/ML connections from the lesson

**Softmax:** uses exponentials to transform model scores into normalized class probabilities.

**Cross-entropy:** for a correct-class predicted probability p, the loss contribution is -log(p). A probability close to 1 gives a small loss; a probability close to 0 gives a large loss.

**Learning-rate decay:** the lesson gives an exponential decay form, LR = LR₀ × e^(-decay × t), where the learning rate decreases over time.

**Log-scale plots:** logarithmic axes can help show changes across values that span a wide range.

## 8. Python observations

The implementation plots 2^x, e^x, x^2, log base 2, ln, and log base 10. It also prints sample calculations. Logarithms are defined only for positive real inputs, so x = 0 is not a valid input for the real-valued logarithm.

Source: Day 3 — Exponents & Logarithms study PDF.
