
import numpy as np

# ==========================================
# 1. DELETE ONE ELEMENT FROM A 1D ARRAY
# ==========================================

arr = np.array([10, 20, 30, 40, 50])

result = np.delete(arr, 2)

print("1. Delete one element:")
print(result)
# [10 20 40 50]


# ==========================================
# 2. DELETE MULTIPLE ELEMENTS
# ==========================================

arr = np.array([10, 20, 30, 40, 50])

result = np.delete(arr, [1, 3])

print("\n2. Delete multiple elements:")
print(result)
# [10 30 50]


# ==========================================
# 3. DELETE USING A RANGE OF INDICES
# ==========================================

arr = np.array([10, 20, 30, 40, 50, 60])

result = np.delete(arr, np.arange(1, 4))

print("\n3. Delete indices 1, 2, and 3:")
print(result)
# [10 50 60]


# ==========================================
# 4. DELETE A ROW (axis=0)
# ==========================================

arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

result = np.delete(arr, 1, axis=0)

print("\n4. Delete row index 1:")
print(result)
# [[1 2 3]
#  [7 8 9]]


# ==========================================
# 5. DELETE A COLUMN (axis=1)
# ==========================================

arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

result = np.delete(arr, 1, axis=1)

print("\n5. Delete column index 1:")
print(result)
# [[1 3]
#  [4 6]
#  [7 9]]


# ==========================================
# 6. DELETE MULTIPLE ROWS
# ==========================================

arr = np.array([
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8]
])

result = np.delete(arr, [0, 2], axis=0)

print("\n6. Delete rows 0 and 2:")
print(result)
# [[3 4]
#  [7 8]]


# ==========================================
# 7. DELETE MULTIPLE COLUMNS
# ==========================================

arr = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])

result = np.delete(arr, [0, 2], axis=1)

print("\n7. Delete columns 0 and 2:")
print(result)
# [[2 4]
#  [6 8]]


# ==========================================
# 8. DELETE WITHOUT SPECIFYING AXIS
# ==========================================

arr = np.array([
    [1, 2],
    [3, 4]
])

result = np.delete(arr, 1)

print("\n8. Delete from flattened array:")
print(result)
# [1 3 4]


# ==========================================
# 9. np.zeros()
# CREATE AN ARRAY FILLED WITH ZEROS
# ==========================================

zeros_1d = np.zeros(5)

print("\n9. One-dimensional zeros:")
print(zeros_1d)
# [0. 0. 0. 0. 0.]


# ==========================================
# 10. np.zeros() WITH TWO DIMENSIONS
# ==========================================

zeros_2d = np.zeros((3, 4))

print("\n10. Two-dimensional zeros:")
print(zeros_2d)
# Three rows and four columns


# ==========================================
# 11. np.zeros() WITH INTEGER DATA TYPE
# ==========================================

zeros_int = np.zeros((2, 3), dtype=int)

print("\n11. Integer zeros:")
print(zeros_int)
# [[0 0 0]
#  [0 0 0]]


# ==========================================
# 12. DELETE FROM AN ARRAY CREATED WITH ZEROS
# ==========================================

arr = np.zeros((3, 3), dtype=int)

arr[0] = [1, 2, 3]
arr[1] = [4, 5, 6]
arr[2] = [7, 8, 9]

result = np.delete(arr, 1, axis=0)

print("\n12. Delete a row from the array:")
print(result)
# [[1 2 3]
#  [7 8 9]]


# ==========================================
# 13. THE ORIGINAL ARRAY IS NOT CHANGED
# ==========================================

arr = np.array([10, 20, 30, 40])

result = np.delete(arr, 1)

print("\n13. Original array:")
print(arr)
# [10 20 30 40]

print("New array:")
print(result)
# [10 30 40]


# ==========================================
# 14. CHECK ARRAY SHAPES AFTER DELETION
# ==========================================

arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("\n14. Original shape:")
print(arr.shape)
# (3, 3)

result = np.delete(arr, 0, axis=0)

print("Shape after deleting a row:")
print(result.shape)
# (2, 3)

result = np.delete(arr, 0, axis=1)

print("Shape after deleting a column:")
print(result.shape)
# (3, 2)
