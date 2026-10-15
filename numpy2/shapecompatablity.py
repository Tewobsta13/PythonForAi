
import numpy as np

# ==========================================
# 1. UNDERSTANDING ARRAY SHAPES
# ==========================================

a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("Array a:")
print(a)

print("Shape of a:", a.shape)  # (2, 3)
print("Dimensions:", a.ndim)    # 2


# ==========================================
# 2. SAME SHAPE: ADDITION
# ==========================================

a = np.array([
    [1, 2],
    [3, 4]
])

b = np.array([
    [10, 20],
    [30, 40]
])

print("\nSame shape addition:")
print("Shape of a:", a.shape)  # (2, 2)
print("Shape of b:", b.shape)  # (2, 2)
print(a + b)


# ==========================================
# 3. BROADCASTING: 2D + 1D
# ==========================================

a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])  # Shape (2, 3)

b = np.array([10, 20, 30])  # Shape (3,)

print("\nBroadcasting example:")
print("Shape of a:", a.shape)
print("Shape of b:", b.shape)
print(a + b)

# Output:
# [[11 22 33]
#  [14 25 36]]


# ==========================================
# 4. BROADCASTING WITH A DIMENSION OF 1
# ==========================================

a = np.array([
    [1],
    [2],
    [3]
])  # Shape (3, 1)

b = np.array([10, 20])  # Shape (2,)

print("\nBroadcasting (3, 1) + (2,):")
print("Shape of a:", a.shape)
print("Shape of b:", b.shape)
print(a + b)

# Output:
# [[11 21]
#  [12 22]
#  [13 23]]
# Result shape: (3, 2)


# ==========================================
# 5. INCOMPATIBLE SHAPES
# ==========================================

a = np.array([
    [1, 2],
    [3, 4]
])  # Shape (2, 2)

b = np.array([10, 20, 30])  # Shape (3,)

print("\nIncompatible shapes example:")
print("Shape of a:", a.shape)
print("Shape of b:", b.shape)

try:
    print(a + b)
except ValueError as error:
    print("Error:", error)


# ==========================================
# 6. CHECK SHAPE COMPATIBILITY
# ==========================================

def check_broadcasting(shape_a, shape_b):
    """
    Check whether two shapes are compatible
    for NumPy broadcasting.
    """

    a_dims = list(shape_a)
    b_dims = list(shape_b)

    # Add dimensions of size 1 to the left
    # until both shapes have equal length.
    max_dims = max(len(a_dims), len(b_dims))

    a_dims = [1] * (max_dims - len(a_dims)) + a_dims
    b_dims = [1] * (max_dims - len(b_dims)) + b_dims

    # Compare dimensions from left to right
    # after aligning them from the right.
    for dim_a, dim_b in zip(a_dims, b_dims):
        if dim_a != dim_b and dim_a != 1 and dim_b != 1:
            return False

    return True


print("\nCompatibility checks:")

print(check_broadcasting((2, 3), (2, 3)))  # True
print(check_broadcasting((2, 3), (3,)))    # True
print(check_broadcasting((2, 3), (2, 1)))  # True
print(check_broadcasting((2, 3), (2,)))    # False
print(check_broadcasting((3, 4), (2, 4)))  # False


# ==========================================
# 7. PRACTICE
# ==========================================

print("\nPractice: determine whether these shapes work.")

shapes = [
    ((4, 3), (3,)),
    ((5, 1), (1, 6)),
    ((2, 3), (2,)),
    ((3, 1), (3,)),
    ((2, 3, 4), (3, 4)),
]

for shape_a, shape_b in shapes:
    compatible = check_broadcasting(shape_a, shape_b)

    print(
        f"{shape_a} and {shape_b}: "
        f"{'Compatible' if compatible else 'Incompatible'}"
    )
