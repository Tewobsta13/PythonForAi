import numpy as np

# ==========================================
# NUMPY: VECTORIZED OPERATIONS
# ==========================================

# Vectorized operations allow us to perform
# calculations on every array element at once
# without writing an explicit Python loop.


# ------------------------------------------
# 1. NORMAL PYTHON WAY (USING A LOOP)
# ------------------------------------------

numbers = [10, 20, 30, 40]

result = []

for number in numbers:
    result.append(number * 2)

print("Using a Python loop:")
print(result)
# Output: [20, 40, 60, 80]


# ------------------------------------------
# 2. VECTORIZED OPERATIONS WITH NUMPY
# ------------------------------------------

arr = np.array([10, 20, 30, 40])

# Multiply every element by 2
print("\nMultiplication:")
print(arr * 2)
# Output: [20 40 60 80]

# Add 5 to every element
print("\nAddition:")
print(arr + 5)
# Output: [15 25 35 45]

# Subtract 5 from every element
print("\nSubtraction:")
print(arr - 5)
# Output: [ 5 15 25 35]

# Divide every element by 10
print("\nDivision:")
print(arr / 10)
# Output: [1. 2. 3. 4.]

# Raise every element to the power of 2
print("\nPower:")
print(arr ** 2)
# Output: [ 100  400  900 1600]


# ------------------------------------------
# 3. OPERATIONS BETWEEN TWO ARRAYS
# ------------------------------------------

a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

# Add corresponding elements
print("\nAdding two arrays:")
print(a + b)
# Output: [11 22 33]

# Subtract corresponding elements
print("\nSubtracting two arrays:")
print(a - b)
# Output: [ 9 18 27]

# Multiply corresponding elements
print("\nMultiplying two arrays:")
print(a * b)
# Output: [10 40 90]

# Divide corresponding elements
print("\nDividing two arrays:")
print(a / b)
# Output: [10. 10. 10.]


# ------------------------------------------
# 4. VECTORIZED OPERATIONS WITH A 2D ARRAY
# ------------------------------------------

arr_2d = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

# Multiply every element by 2
print("\n2D array multiplied by 2:")
print(arr_2d * 2)
# Output:
# [[ 20  40  60]
#  [ 80 100 120]]

# Add 10 to every element
print("\n2D array plus 10:")
print(arr_2d + 10)
# Output:
# [[20 30 40]
#  [50 60 70]]


# ------------------------------------------
# 5. COMPARISON OPERATIONS
# ------------------------------------------

arr = np.array([10, 20, 30, 40])

# Check each element to see whether it is greater than 20
print("\nElements greater than 20:")
print(arr > 20)
# Output: [False False  True  True]

# Check which elements are equal to 20
print("\nElements equal to 20:")
print(arr == 20)
# Output: [False  True False False]


# ------------------------------------------
# 6. USING A CONDITION TO FILTER ELEMENTS
# ------------------------------------------

arr = np.array([10, 20, 30, 40, 50])

# Keep only elements greater than 25
result = arr[arr > 25]

print("\nElements greater than 25:")
print(result)
# Output: [30 40 50]

# ------------------------------------------
# 7. WHY VECTORIZATION IS USEFUL IN AI
# ------------------------------------------

# Example: scale data by dividing every value by 100

data = np.array([25, 50, 75, 100])

scaled_data = data / 100

print("\nScaled data:")
print(scaled_data)
# Output: [0.25 0.5  0.75 1.  ]

# This kind of operation is useful when preparing
# data for machine learning models.
# Create a one-dimensional array
arr = np.array([1, 2, 3, 4, 5])

# Create a normal Python function
def square(x):
    return x ** 2

# Convert the function into a NumPy vectorized function
vectorized_square = np.vectorize(square)

# Apply the function to every element
result = vectorized_square(arr)

print(result)
# Output: [ 1  4  9 16 25]

#compatablity rule 