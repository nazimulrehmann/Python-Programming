# Mathematical Constants
# This guide covers the complete math module with practical applications, performance considerations, 
# and advanced usage patterns for scientific computing, data analysis, and engineering applications.

# Basic Understanding of the Math function:

import math

# Constants
print(math.pi)     # 3.141592653589793
print(math.e)      # 2.718281828459045
print(math.tau)    # 6.283185307179586 (2*pi)
print(math.inf)    # inf
print(math.nan)    # nan

# Basic functions
print(math.sqrt(16))      # 4.0
print(math.pow(2, 3))     # 8.0
print(math.exp(1))        # e^1 ≈ 2.718
print(math.log(100, 10))  # 2.0 (log base 10)

# Trigonometric functions (in radians)
angle = math.pi / 4  # 45 degrees
print(math.sin(angle))     # ≈0.707
print(math.cos(angle))     # ≈0.707
print(math.tan(angle))     # ≈1.0
print(math.degrees(angle)) # 45.0

# Advanced functions
print(math.gcd(48, 18))           # 6
print(math.comb(5, 2))            # 10 (n choose k)
print(math.perm(5, 2))            # 20 (n permute k)
print(math.dist((0,0), (3,4)))    # 5.0 (Euclidean distance)
print(math.prod([2, 3, 4]))       # 24 (product of iterable)



# Advanced view of the Math Functions:

# Standard constants
print(f"π: {math.pi:.15f}")       # 3.141592653589793
print(f"e: {math.e:.15f}")        # 2.718281828459045
print(f"τ (2π): {math.tau:.15f}") # 6.283185307179586

# Special values
print(f"Positive infinity: {math.inf}")
print(f"Negative infinity: {-math.inf}")
print(f"Not a number: {math.nan}")

# IEEE 754 special values
print(f"math.isfinite(inf): {math.isfinite(math.inf)}")  # False
print(f"math.isnan(nan): {math.isnan(math.nan)}")        # True


# Number-Theoretic and Representation Functions

# Floating-point manipulation
x = 3.14159
print(f"math.floor({x}): {math.floor(x)}")      # 3
print(f"math.ceil({x}): {math.ceil(x)}")        # 4
print(f"math.trunc({x}): {math.trunc(x)}")      # 3
print(f"math.modf({x}): {math.modf(x)}")        # (0.14159, 3.0)

# Absolute value and sign
print(f"math.fabs(-{x}): {math.fabs(-x)}")      # 3.14159
print(f"math.copysign(-{x}, 1): {math.copysign(-x, 1)}")  # 3.14159

# GCD and LCM
print(f"math.gcd(48, 18): {math.gcd(48, 18)}")  # 6
print(f"math.lcm(15, 20): {math.lcm(15, 20)}")  # 60 (Python 3.9+)

# Factorials and combinatorics
print(f"10! = {math.factorial(10)}")            # 3628800
print(f"C(5,2) = {math.comb(5, 2)}")            # 10
print(f"P(5,2) = {math.perm(5, 2)}")            # 20



# Power and Logarithmic Functions

# Exponential functions
print(f"e^2 = {math.exp(2):.6f}")               # 7.389056
print(f"2^3 = {math.pow(2, 3)}")                # 8.0
print(f"math.expm1(1e-10): {math.expm1(1e-10)}") # More accurate for small x

# Logarithmic functions
print(f"ln(10) = {math.log(10):.6f}")           # 2.302585
print(f"log2(1024) = {math.log2(1024)}")        # 10.0
print(f"log10(1000) = {math.log10(1000)}")      # 3.0
print(f"log(125, 5) = {math.log(125, 5)}")      # 3.0

# Special logarithmic functions
print(f"math.log1p(1e-10): {math.log1p(1e-10)}") # More accurate near 1


# Trigonometric and Hyperbolic Functions

angle_deg = 45
angle_rad = math.radians(angle_deg)

print(f"sin({angle_deg}°) = {math.sin(angle_rad):.6f}")  # 0.707107
print(f"cos({angle_deg}°) = {math.cos(angle_rad):.6f}")  # 0.707107
print(f"tan({angle_deg}°) = {math.tan(angle_rad):.6f}")  # 1.000000

# Inverse functions
print(f"asin(0.5) = {math.degrees(math.asin(0.5)):.2f}°")  # 30.00°
print(f"acos(0.5) = {math.degrees(math.acos(0.5)):.2f}°")  # 60.00°
print(f"atan(1) = {math.degrees(math.atan(1)):.2f}°")      # 45.00°

# Hypotenuse calculation
print(f"hypot(3, 4) = {math.hypot(3, 4)}")      # 5.0


# Advanced Trigonometry

# Angular conversions
print(f"90° in radians: {math.radians(90):.6f}")  # 1.570796
print(f"π/2 in degrees: {math.degrees(math.pi/2)}")  # 90.0

# Hyperbolic functions
x = 1.0
print(f"sinh({x}) = {math.sinh(x):.6f}")        # 1.175201
print(f"cosh({x}) = {math.cosh(x):.6f}")        # 1.543081
print(f"tanh({x}) = {math.tanh(x):.6f}")        # 0.761594

# Inverse hyperbolic
print(f"asinh(1.175) ≈ {math.asinh(1.175):.3f}")  # ≈1.0
print(f"acosh(1.543) ≈ {math.acosh(1.543):.3f}")  # ≈1.0


# Special Functions and Distance Calculations

# Gamma and related functions
print(f"Γ(5) = {math.gamma(5)}")                # 24.0 (same as 4!)
print(f"ln|Γ(5)| = {math.lgamma(5)}")           # ln(24)
print(f"erf(1) = {math.erf(1):.6f}")            # 0.842701
print(f"erfc(1) = {math.erfc(1):.6f}")          # 0.157299

# Distance calculations
point1 = (1, 2, 3)
point2 = (4, 6, 9)
print(f"Euclidean distance: {math.dist(point1, point2):.6f}")  # 7.810250

# Product of iterables
print(f"Product of range(1,6): {math.prod(range(1,6))}")  # 120 (1*2*3*4*5)


# Numerical Stability Considerations
# Comparing exp implementations
x = 1e-10
print(f"exp({x})-1 = {math.exp(x)-1}")          # 0.0 (loss of precision)
print(f"expm1({x}) = {math.expm1(x)}")          # 1.00000000005e-10 (accurate)

# Accurate hypotenuse for large numbers
large = 1e200
print(f"Naive sqrt(x²+y²): {math.sqrt(large**2 + large**2)}")  # inf
print(f"math.hypot: {math.hypot(large, large)}")               # 1.4142e+200


# Precision Considerations:

# Bad: Comparing floats directly
if math.sin(math.pi) == 0:  # Likely False
    print("Exactly zero")

# Good: Use math.isclose()
if math.isclose(math.sin(math.pi), 0, abs_tol=1e-9):
    print("Effectively zero")

# Performance Tips
# Cache frequently used constants
TWOPI = math.tau
INV_PI = 1 / math.pi

# Precompute expensive operations
SIN_30 = math.sin(math.radians(30))



# Domain Awareness:
# Handle edge cases
def safe_acos(x):
    x = max(-1.0, min(1.0, x))  # Clamp to valid range
    return math.acos(x)

# Using with random module
import random
def random_unit_vector():
    angle = random.uniform(0, math.tau)
    return (math.cos(angle), math.sin(angle))





