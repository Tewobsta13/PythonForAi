
import numpy as np
scores = np.array([85, 92, 78, 95, 88])
print(scores)
#(),[]  
print(type(scores))
numbers = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print(numbers)
# Python lists are general-purpose and can store different types of data.
# NumPy arrays are designed for numerical data and allow faster mathematical operations.
# Check the number of dimensions of the array
print(numbers.ndim)

# Check the data type of the elements in the array
print(numbers.dtype)

# Check the type of the NumPy object
print(type(numbers))
numbers = np.array([10, 20, 30], dtype=np.int8)#memory it uses now decreases

number = np.array([
    [True, False, True],
    [False, True, False]
])

print(number)
print(number.dtype)
print(number.ndim)
print(number.shape)


temperatures = np.array([
    [24.5, 25.7, 26.3],
    [23.8, 24.9, 27.1]
], dtype=np.float32)

print(temperatures)
print(temperatures.dtype)
print(temperatures.ndim)
print(temperatures.shape)
import numpy as np

# NumPy arrays normally contain one data type.
# When different data types are mixed, NumPy converts them
# to a common data type.

data = np.array([10, 3.5, True, "Hey"])

print(data)
print(data.dtype)
# Integer and float are mixed, so NumPy converts the integer to a float.

data = np.array([10, 3.5])

print(data)
print(data.dtype)
import numpy as np

# Create a 3D array with 3 layers, 3 rows, and 3 columns
data = np.array([
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ],
    [
        [10, 11, 12],
        [13, 14, 15],
        [16, 17, 18]
    ],
    [
        [19, 20, 21],
        [22, 23, 24],
        [25, 26, 27]
    ]
], dtype=int)

print(data)
print(data.ndim)
print(data.shape)
print(data.dtype)
# Create numbers from 0 up to, but not including, 10
# np.arange() creates a sequence of numbers
numbers = np.arange(2, 10, 2)


# np.random.rand() creates random decimal numbers between 0 and 1
random_numbers = np.random.rand(5)

# np.random.randint() creates random integers within a specified range
random_integers = np.random.randint(1, 11, 5)

# Create numbers from -5 up to, but not including, 5
numbers = np.arange(-5, 5)

print(numbers)




# Create a 2D array
array_2d = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# Create a 3D array using the 2D array
array_3d = np.array([
    array_2d,
    array_2d,
    array_2d
])

print(array_3d)
print(array_3d.shape)
#typecoersion