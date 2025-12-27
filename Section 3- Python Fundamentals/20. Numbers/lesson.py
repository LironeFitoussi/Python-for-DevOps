# Python Fundamentals: Working with Numbers and Arithmetic

# Numeric Types in Python
# Check a variable's type with the built-in type() function
type(1)     # <class 'int'>
type(1.0)   # <class 'float'>

# Floating-Point Precision Issue
# Python uses IEEE 754 standard for floating-point arithmetic, which can introduce tiny rounding errors
print(0.1 * 3 == 0.3)  # False!

# Solution: Use math.isclose()
import math

print(math.isclose(0.1 * 3, 0.3))  # True

# True Division Always Returns Float
print(8 / 2)       # 4.0
type(8 / 2)        # <class 'float'>

# Floor Division Rounds Down
print(7 // 2)      # 3
print(7.0 // 2)    # 3.0

# Modulus Operator: %
# Returns the remainder of a division
print(5 % 3)  # 2

# Example: Cycling Through Indexes
# If you want to ensure an index always stays within the range 0–2 (e.g., for a list of 3 items):
print(5 % 3)   # 2
print(6 % 3)   # 0
print(7 % 3)   # 1
print(8 % 3)   # 2

