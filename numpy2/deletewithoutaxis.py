
import numpy as np

# ==========================================
# 1. CREATE A 1D ARRAY
# ==========================================

arr = np.array([10, 20, 30, 40, 50])

print("Original array:")
print(arr)

# ==========================================
# 2. DELETE ONE ELEMENT
# ==========================================

result = np.delete(arr, 2)

print("\nDelete index 2:")
print(result)
# [10 20 40 50]


# ==========================================
# 3. DELETE MULTIPLE ELEMENTS
# ==========================================

arr = np.array([10, 20, 30, 40, 50])

result = np.delete(arr, [0, 2, 4])

print("\nDelete indices 0, 2, and 4:")
print(result)
# [20 40]


# ==========================================
# 4. DELETE FROM A 2D ARRAY WITHOUT AXIS
# ==========================================

arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("\nOriginal 2D array:")
print(arr)

result = np.delete(arr, 4)

print("\nDelete flattened index 4:")
print(result)
# [1 2 3 4 6 7 8 9]


# ==========================================
# 5. UNDERSTAND FLATTENING
# ==========================================

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

flat = arr.flatten()

print("\nFlattened array:")
print(flat)
# [10 20 30 40 50 60]

result = np.delete(arr, 3)

print("\nDelete index 3 without axis:")
print(result)
# [10 20 30 50 60]


# ==========================================
# 6. DELETE MULTIPLE INDICES FROM A 2D ARRAY
# ==========================================

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

result = np.delete(arr, [1, 4])

print("\nDelete flattened indices 1 and 4:")
print(result)
# [1 3 4 6]


# ==========================================
# 7. DELETE USING np.arange()
# ==========================================

arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

# Delete flattened indices 2, 3, and 4
indices = np.arange(2, 5)

result = np.delete(arr, indices)

print("\nDelete indices 2 through 4:")
print(result)
# [10 20 60 70 80 90]


# ==========================================
# 8. NEGATIVE INDICES
# ==========================================

arr = np.array([10, 20, 30, 40, 50])

result = np.delete(arr, -1)

print("\nDelete the last element:")
print(result)
# [10 20 30 40]


# ==========================================
# 9. DELETE THE FIRST AND LAST ELEMENTS
# ==========================================

arr = np.array([10, 20, 30, 40, 50])

result = np.delete(arr, [0, -1])

print("\nDelete first and last:")
print(result)
# [20 30 40]


# ==========================================
# 10. ORIGINAL ARRAY STAYS UNCHANGED
# ==========================================

arr = np.array([
    [1, 2],
    [3, 4]
])

result = np.delete(arr, 1)

print("\nOriginal array:")
print(arr)
# [[1 2]
#  [3 4]]

print("Result after deletion:")
print(result)
# [1 3 4]


# ==========================================
# 11. CHECK THE SHAPE
# ==========================================

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("\nOriginal shape:")
print(arr.shape)
# (2, 3)

result = np.delete(arr, 1)

print("Result shape:")
print(result.shape)
# (5,)


# ==========================================
# 12. COMPARE delete() AND flatten()
# ==========================================

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

flat = arr.flatten()

print("\nUsing flatten():")
print(flat)
# [1 2 3 4 5 6]

print("\nUsing delete() without axis:")
print(np.delete(arr, 2))
# [1 2 4 5 6]

print("\nFlatten first, then delete:")
print(np.delete(flat, 2))
# [1 2 4 5 6]
