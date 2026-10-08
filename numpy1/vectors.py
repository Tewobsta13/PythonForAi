import numpy as np
#num py vertical and horizontal 1d is the same

arr = np.array([1, 2, 3, 4])
print(arr.shape)
# 5 rows and 1 column (vertical)
vertical = np.array([
    [1],
    [2],
    [3],
    [4],
    [5]
])

# 1 row and 5 columns (horizontal)
horizontal = np.array([
    [1, 2, 3, 4, 5]
])

print("Vertical:")
print(vertical)
print("Shape:", vertical.shape)

print("\nHorizontal:")
print(horizontal)
print("Shape:", horizontal.shape)
#flatten
array = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

flat = array.flatten()

print(flat)
print(flat.shape)
#reshape
numbers = np.array([1, 2, 3, 4, 5, 6])

new_array = numbers.reshape(2, 3)

print(new_array)

#indexing
numbers = np.array([
    [5, 10, 15],
    [20, 25, 30],
    [35, 40, 45]
])

print(numbers[2, 1])
#differrent indexing
numbers = np.array([
    [0, 1, 2, 3, 4, 5, 6],
    [10, 11, 12, 13, 14, 15, 16],
    [20, 21, 22, 23, 24, 25, 26]
])

print(numbers[:, 3:6:2])
#sort
#sort by axix
#filtering arrays

numbers = np.array([1, 2, 3, 4, 5, 6])

mask = numbers % 2 == 0

print(mask)