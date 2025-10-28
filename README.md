# Computational Number Theory Algorithms

This repository contains laboratory work #1 as part of a third-year Number-theoretic methods in cryptography course at Peter the Great St. Petersburg Polytechnic University (SPbPU).
A collection of efficient algorithms for number theory computations with detailed step-by-step execution tracking.

## Algorithms Implemented

### 1. Extended Euclidean Algorithm
- Computes GCD of two integers
- Finds Bézout coefficients (x, y) such that `a*x + b*y = gcd(a,b)`
- Displays all intermediate steps with remainders and coefficients

### 2. Binary Extended Euclidean Algorithm  
- Optimized version using bit shifts and subtractions
- More efficient for computer implementation
- Maintains coefficients throughout the computation

### 3. Euclidean Algorithm with "Truncated" Remainders

## Usage

```python
# Extended Euclidean Algorithm
python euclidean.py

# Binary Extended Euclidean Algorithm  
python bin_euclidean.py

# Euclidean Algorithm with "Truncated" Remainders
python remn_euclidean.py

# Example input:
19387226047544992493
19387207028695801417
