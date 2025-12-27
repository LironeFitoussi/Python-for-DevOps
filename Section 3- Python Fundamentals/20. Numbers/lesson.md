# 🔢 Python Fundamentals: Working with Numbers and Arithmetic

In this lesson, we dive into **numeric types** in Python and explore both **basic arithmetic operations** and some of Python’s more **subtle behavior** around numbers, especially floating-point precision.

---

## 🧮 Numeric Types in Python

Python supports two main numeric types:

| Type    | Description                     | Example               |
| ------- | ------------------------------- | --------------------- |
| `int`   | Integer (whole number)          | `1`, `200`, `-5`      |
| `float` | Floating point (decimal number) | `1.0`, `3.14`, `-0.5` |

You can check a variable’s type with the built-in `type()` function:

```python
type(1)     # <class 'int'>
type(1.0)   # <class 'float'>
```

---

## ⚠️ Floating-Point Precision Issue

Python (like most programming languages) uses IEEE 754 standard for floating-point arithmetic, which can introduce **tiny rounding errors**.

### 🔍 Example:

```python
print(0.1 * 3 == 0.3)  # False!
```

This evaluates to `False` due to floating-point imprecision.

### ✅ Solution: Use `math.isclose()`

```python
import math

print(math.isclose(0.1 * 3, 0.3))  # True
```

This method safely compares floats by allowing for small differences in precision.

---

## ➗ Arithmetic Operations in Python

| Operator | Description             | Example  | Result        |
| -------- | ----------------------- | -------- | ------------- |
| `+`      | Addition                | `3 + 2`  | `5`           |
| `-`      | Subtraction             | `5 - 3`  | `2`           |
| `*`      | Multiplication          | `4 * 2`  | `8`           |
| `/`      | **True Division**       | `7 / 2`  | `3.5` (float) |
| `//`     | **Floor Division**      | `7 // 2` | `3` (int)     |
| `%`      | **Modulus (Remainder)** | `7 % 2`  | `1`           |
| `**`     | Exponentiation          | `2 ** 3` | `8`           |

### 🔸 True Division Always Returns Float

```python
print(8 / 2)       # 4.0
type(8 / 2)        # <class 'float'>
```

### 🔸 Floor Division Rounds Down

```python
print(7 // 2)      # 3
print(7.0 // 2)    # 3.0
```

* If either operand is a float, the result is a float.
* Otherwise, it returns an integer.

---

## 🧮 Modulus Operator: `%`

Returns the **remainder** of a division.

```python
print(5 % 3)  # 2
```

This is especially useful for **cycling through a fixed range** of values.

### 🔁 Example: Cycling Through Indexes

If you want to ensure an index always stays within the range `0–2` (e.g., for a list of 3 items):

```python
print(5 % 3)   # 2
print(6 % 3)   # 0
print(7 % 3)   # 1
print(8 % 3)   # 2
```

This pattern repeats: `2 → 0 → 1 → 2 → ...`

---

## 🧠 Summary

* Python supports `int` and `float` numeric types.
* Floating-point operations may have **rounding errors** — use `math.isclose()` for safe comparison.
* Use `/` for float division, `//` for integer (floor) division.
* `%` helps in cycling or getting remainders — useful in list indexing and control flow.

> These foundational operations are essential for DevOps scripting, especially when dealing with loop counters, API rate limits, and conditional checks based on numerical values.

Coming up next: we’ll explore **strings and text manipulation** in Python!
