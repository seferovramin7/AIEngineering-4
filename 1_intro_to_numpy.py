# 1_intro_to_numpy.py
# TOPIC: The fundamentals of NumPy for numerical data.

# First, we need to import the NumPy library.
# We use 'as np' as a standard shorthand to make our code cleaner.
import numpy as np

print("----------- Part 1: Why NumPy? -----------")
# NumPy provides a high-performance array object called 'ndarray'.
# It's much faster and more efficient than standard Python lists for numerical operations.
# This is crucial for AI and Machine Learning, which involve heavy calculations.


print("\n----------- Part 2: Creating NumPy Arrays -----------")
# From a Python list
list_a = [1, 2, 3, 4, 5]
np_array_a = np.array(list_a)
print(f"Array from a list: {np_array_a}")

# Create an array of all zeros (e.g., to initialize weights in a neural network)
zeros_array = np.zeros((2, 3)) # A 2x3 array (2 rows, 3 columns)
print("An array of zeros:")
print(zeros_array)

# Create an array of all ones
ones_array = np.ones((2,3))
print("An array of ones:")
print(ones_array)

# Create an array with a range of numbers
range_array = np.arange(0, 10, 3) # Start at 0, end before 10, step by 2
print(f"An array with a range of numbers: {range_array}")


print("\n----------- Part 3: Array Attributes -----------")
# We can inspect the properties of our arrays.
print(f"Array: {np_array_a}")
print(f"Shape of the array: {np_array_a.shape}") # Tells us the dimensions
print(f"Number of dimensions: {zeros_array.ndim}") # 1-dimensional
print(f"Data type of elements: {np_array_a.dtype}") # e.g., int64, float64

print(f"\nShape of our 2x3 zeros array: {zeros_array.shape}")
print(f"Number of dimensions: {zeros_array.ndim}") # 2-dimensional


print("\n----------- Part 4: Indexing and Slicing -----------")
# Just like lists, we can access elements of an array.
numbers = np.arange(10, 20)
print(f"Original array: {numbers}")
print(f"Element at index 3: {numbers[3]}") # Gets the 4th element (13)
print(f"Elements from index 2 to 5: {numbers[2:6]}") # Slicing

# Boolean Indexing - a very powerful way to filter data
# Find all numbers in the array that are greater than 15
greater_than_15 = numbers[numbers > 15]
print(f"Numbers greater than 15: {greater_than_15}")


print("\n----------- Part 5: Vectorized Operations -----------")
# NumPy allows you to perform operations on entire arrays at once, which is super fast.
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# No need for loops!
addition = arr1 + arr2
print(f"Element-wise addition: {addition}")

multiplication = arr1 * 10
print(f"Element-wise multiplication: {multiplication}")


print("\n----------- Part 6: Basic Aggregations -----------")
# We can easily calculate summary statistics.
data_points = np.array([5, 10, 15, 20, 25])
print(f"Data: {data_points}")
print(f"Sum of all points: {np.sum(data_points)}") # or data_points.sum()
print(f"Mean (average) of all points: {np.mean(data_points)}")
print(f"Maximum value: {np.max(data_points)}")
print(f"Minimum value: {np.min(data_points)}")

print("\nNumPy is the foundation. Now let's see how Pandas builds on it for data analysis!")