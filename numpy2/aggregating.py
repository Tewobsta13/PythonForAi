
import numpy as np

# ==========================================
# NUMPY AGGREGATION METHODS
# ==========================================

# Aggregation means summarizing multiple values
# into one result.

arr = np.array([10, 20, 30, 40, 50])

# 1. SUM: Adds all elements
print(np.sum(arr))       # 150
print(arr.sum())         # 150

# 2. MEAN: Calculates the average
print(np.mean(arr))      # 30.0

# 3. MEDIAN: Returns the middle value
print(np.median(arr))    # 30.0

# 4. MIN: Returns the smallest value
print(np.min(arr))       # 10

# 5. MAX: Returns the largest value
print(np.max(arr))       # 50

# 6. STANDARD DEVIATION: Measures spread around the mean
print(np.std(arr))       # 14.1421356237...

# 7. VARIANCE: Measures the average squared deviation
# from the mean (population variance by default)
print(np.var(arr))       # 200.0

# 8. PRODUCT: Multiplies all elements
print(np.prod(arr))      # 12000000

# 9. ARGMIN: Returns the index of the minimum value
print(np.argmin(arr))    # 0

# 10. ARGMAX: Returns the index of the maximum value
print(np.argmax(arr))    # 4

# 11. COUNT NONZERO: Counts elements that are not zero
arr2 = np.array([0, 2, 0, 4, 5])
print(np.count_nonzero(arr2))  # 3

# 12. CUMSUM: Calculates the cumulative sum
print(np.cumsum(arr))    # [10 30 60 100 150]

# 13. CUMPROD: Calculates the cumulative product
print(np.cumprod(np.array([1, 2, 3, 4])))
# [1 2 6 24]


# ==========================================
# AGGREGATION WITH 2D ARRAYS
# ==========================================

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# Aggregate the entire array
print(np.sum(arr))       # 21
print(np.mean(arr))      # 3.5
print(np.min(arr))       # 1
print(np.max(arr))       # 6

# axis=0: Aggregate down the rows, producing one result per column
print(np.sum(arr, axis=0))
# [5 7 9]

# axis=1: Aggregate across the columns, producing one result per row
print(np.sum(arr, axis=1))
# [ 6 15]

# Other examples with axes
print(np.mean(arr, axis=0))  # [2.5 3.5 4.5]
print(np.max(arr, axis=1))   # [3 6]
print(np.min(arr, axis=0))   # [1 2 3]


# ==========================================
# KEEP DIMENSIONS
# ==========================================

# keepdims=True preserves the reduced dimensions
print(np.sum(arr, axis=0, keepdims=True))
# [[5 7 9]] -- shape (1, 3)

print(np.sum(arr, axis=1, keepdims=True))
# [[ 6]
#  [15]] -- shape (2, 1)

import numpy as np

# ==========================================
# NUMPY AGGREGATION METHODS USING A 2D ARRAY
# ==========================================

arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("Original array:")
print(arr)

# axis=None (default): Aggregate the entire array

# 1. SUM: Adds all elements
print("Sum:", np.sum(arr))                 # 450

# 2. MEAN: Calculates the average
print("Mean:", np.mean(arr))               # 50.0

# 3. MEDIAN: Returns the middle value
print("Median:", np.median(arr))           # 50.0

# 4. MIN: Returns the smallest element
print("Minimum:", np.min(arr))             # 10

# 5. MAX: Returns the largest element
print("Maximum:", np.max(arr))             # 90

# 6. STANDARD DEVIATION: Measures spread around the mean
print("Standard deviation:", np.std(arr))  # Approximately 25.82

# 7. VARIANCE: Measures squared spread around the mean
print("Variance:", np.var(arr))            # 666.666...

# 8. PRODUCT: Multiplies all elements
print("Product:", np.prod(arr))

# 9. ARGMIN: Index of the minimum in the flattened array
print("Argmin:", np.argmin(arr))           # 0

# 10. ARGMAX: Index of the maximum in the flattened array
print("Argmax:", np.argmax(arr))           # 8

# 11. COUNT NONZERO: Counts nonzero elements
print("Nonzero count:", np.count_nonzero(arr))  # 9

# 12. CUMSUM: Cumulative sum over the flattened array
print("Cumulative sum:", np.cumsum(arr))
# [ 10  30  60 100 150 210 280 360 450]

# 13. CUMPROD: Cumulative product over the flattened array
print("Cumulative product:", np.cumprod(arr))


# ==========================================
# axis=0: AGGREGATE DOWN THE ROWS
# Result contains one value per column
# ==========================================

print("\nSum, axis=0:")
print(np.sum(arr, axis=0))
# [120 150 180]

print("Mean, axis=0:")
print(np.mean(arr, axis=0))
# [40. 50. 60.]

print("Minimum, axis=0:")
print(np.min(arr, axis=0))
# [10 20 30]

print("Maximum, axis=0:")
print(np.max(arr, axis=0))
# [70 80 90]

print("Standard deviation, axis=0:")
print(np.std(arr, axis=0))
# [24.494... 24.494... 24.494...]


# ==========================================
# axis=1: AGGREGATE ACROSS THE COLUMNS
# Result contains one value per row
# ==========================================

print("\nSum, axis=1:")
print(np.sum(arr, axis=1))
# [ 60 150 240]

print("Mean, axis=1:")
print(np.mean(arr, axis=1))
# [20. 50. 80.]

print("Minimum, axis=1:")
print(np.min(arr, axis=1))
# [10 40 70]

print("Maximum, axis=1:")
print(np.max(arr, axis=1))
# [30 60 90]

print("Standard deviation, axis=1:")
print(np.std(arr, axis=1))
# [8.164... 8.164... 8.164...]


# ==========================================
# ARGMIN AND ARGMAX WITH AXES
# ==========================================

# Indices of minimum values in each column
print("\nArgmin, axis=0:")
print(np.argmin(arr, axis=0))
# [0 0 0]

# Indices of maximum values in each column
print("Argmax, axis=0:")
print(np.argmax(arr, axis=0))
# [2 2 2]

# Indices of minimum values in each row
print("Argmin, axis=1:")
print(np.argmin(arr, axis=1))
# [0 0 0]

# Indices of maximum values in each row
print("Argmax, axis=1:")
print(np.argmax(arr, axis=1))
# [2 2 2]


# ==========================================
# KEEP DIMENSIONS
# ==========================================

# keepdims=True preserves the number of dimensions

print("\nSum along axis=0 with keepdims:")
print(np.sum(arr, axis=0, keepdims=True))
# [[120 150 180]] -- shape (1, 3)

print("Sum along axis=1 with keepdims:")
print(np.sum(arr, axis=1, keepdims=True))
# [[ 60]
#  [150]
#  [240]] -- shape (3, 1)
arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

result = np.cumsum(arr)

print(result)
# [ 10  30  60 100 150 210 280 360 450]

print(result.shape)
# (9,)